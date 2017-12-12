import hashlib
from infty.users.models import MemberOrganization


def organizations_domains_hashes(salt):
    hashes = str()
    domains = set()

    for member in MemberOrganization.objects.all():
        for domain in domains.union(member.domains):

            domain_hash = hashlib.sha1(
                (salt+domain).encode('utf-8')
            ).hexdigest()

            domains.update(
                {domain_hash}
            )

    return list(domains)
