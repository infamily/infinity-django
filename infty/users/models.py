from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.utils.crypto import get_random_string

@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

class OneTimePassword(models.Model):
    user = models.ForeignKey(User)
    one_time_password = models.CharField(max_length=64, default=get_random_string)
    is_used = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)#put inactive if maximum nmb of attempts was reached or when is_used=True
    login_attempts = models.IntegerField(default=0)#we can limit it in form validation
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.user.username
