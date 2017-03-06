from mozillians.users.models import UserProfile
from mozillians.users.tests import UserFactory
from mozillians.groups.models import Group
from mozillians.groups.tests import GroupFactory


users = UserFactory.create_batch(100)
groups = GroupFactory.create_batch(20)

for group in Group.objects.all():
    for profile in UserProfile.objects.order_by('?')[:50]:
        group.add_member(profile)


