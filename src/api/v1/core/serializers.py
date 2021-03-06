from django.core.urlresolvers import reverse
from langsplit import splitter
from rest_framework import serializers

from api.v1.core.fields import (
    LangSplitField,
    UserField,
    CategoryNameField
)
from core.models import (
    Topic,
    Comment,
)
from meta.models import Type
from transactions.models import ContributionCertificate, Transaction
from users.models import (User, LanguageName)
from trade.models import Reserve
from decimal import Decimal


class TopicParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'url', 'type', 'title', 'body',
                  'languages', 'is_draft')


class TypeParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'url', 'name', 'definition')


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    title = LangSplitField(required=True)

    body = LangSplitField(required=False)

    type = serializers.ChoiceField(choices=Topic.TOPIC_TYPES, required=False)

    owner = UserField(read_only=True)

    editors = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='user-detail',
        queryset=User.objects.all(),
        required=False)

    parents = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='topic-detail',
        queryset=Topic.objects.all(),
        required=False)

    children = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='topic-detail',
        queryset=Topic.objects.all(),
        required=False)

    categories = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='type-detail',
        queryset=Type.objects.categories(),
        required=False)

    # To assign categories as list of arbitrary strings
    categories_str = CategoryNameField(
        write_only=True,
        many=True,
        queryset=Type.objects.categories(),
        required=False
    )

    # To retrieve list of categories names (localized via langsplit)
    categories_names = CategoryNameField(
        read_only=True,
        many=True,
        source='categories',
    )

    class Meta:
        model = Topic
        fields = ('id', 'url', 'type', 'title', 'body', 'owner', 'editors',
                  'parents', 'children', 'categories', 'categories_str', 'categories_names', 'languages', 'is_draft', 'comment_count',
                  'blockchain', 'matched', 'declared', 'created_date', 'updated_date', 'funds','data')

    def process_categories(self, validated_data):
        categories_str = validated_data.pop('categories_str', [])
        categories = validated_data.get('categories', [])
        if categories_str:
            categories.extend(categories_str)
        if categories:
            validated_data['categories'] = categories
        return validated_data

    def create(self, validated_data):
        validated_data = self.process_categories(validated_data)
        return super(TopicSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        validated_data = self.process_categories(validated_data)

        languages = validated_data.get('languages', [])
        body = validated_data.get('body', '')
        title = validated_data.get('title', '')

        if languages:
            # update existing
            original_title = splitter.split(instance.title)
            original_body = splitter.split(instance.body)
            body_updates = splitter.split(body)
            title_updates = splitter.split(title)

            for lang in languages:
                if (lang in title_updates.keys()) and \
                    (lang in body_updates.keys()):
                    original_title.update({lang: title_updates[lang]})
                    original_body.update({lang: body_updates[lang]})

            validated_data['title'] = splitter.convert(original_title, title=True)
            validated_data['body'] = splitter.convert(original_body)

        return super(TopicSerializer, self).update(instance, validated_data)


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    text = LangSplitField(required=True)
    topic = serializers.HyperlinkedRelatedField(
        view_name='topic-detail', queryset=Topic.objects.all())
    owner = UserField(read_only=True)

    def get_text(self, obj):
        lang = self.context['request'].query_params.get('lang')

        if lang:
            split = splitter.split(obj.text)
            return split.get(lang) or 'languages: {}'.format(
                list(split.keys()))

        return obj.text

    class Meta:
        model = Comment
        fields = ('id', 'url', 'topic', 'text', 'claimed_hours',
                  'assumed_hours', 'owner', 'languages', 'matched', 'donated',
                  'remains', 'parent', 'blockchain', 'created_date', 'updated_date')


class UserBalanceSerializer(serializers.HyperlinkedModelSerializer):

    balance = serializers.SerializerMethodField('matched')
    quota = serializers.SerializerMethodField('compute_quota')
    contributions = serializers.SerializerMethodField('contribution_certificates')
    reserve = serializers.SerializerMethodField('compute_reserve')
    credit = serializers.SerializerMethodField('compute_credit')
    claimed = serializers.SerializerMethodField('compute_claimed')

    def matched(self, obj):
        return ContributionCertificate.user_matched(obj)

    def compute_claimed(self, obj):
        return Comment.user_claimed(obj)

    def compute_quota(self, obj):
        return Transaction.user_quota_remains_today(obj)

    def compute_reserve(self, obj):
        return Reserve.user_reserve_remains(obj)

    def compute_credit(self, obj):
        return self.compute_quota(obj) + self.compute_reserve(obj)

    def contribution_certificates(self, obj):
        request = self.context['request']
        protocol = 'http{}://'.format('s' if request.is_secure() else '')
        domain = request.META.get('HTTP_HOST') or ''
        endpoint = reverse('contributioncertificate-list')

        return "{}{}{}?received_by={}".format(protocol, domain, endpoint,
                                              obj.id)
    class Meta:
        model = User
        fields = ('id', 'username', 'balance', 'contributions', 'quota', 'reserve', 'credit', 'claimed')


class LanguageNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LanguageName
        fields = ('lang', 'name', 'enabled')
