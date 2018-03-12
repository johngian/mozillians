from django.db import models
from django.db.models import Q
from django.utils.timezone import now


class AnnouncementManager(models.Manager):
    """Announcements Manager."""
    use_for_related_fields = True

    def published(self):
        """Return published announcements."""
        return (self.filter(publish_from__lte=now())
                    .filter(Q(publish_until__isnull=True) |
                            (Q(publish_until__isnull=False) &
                             Q(publish_until__gt=now()))))

    def unpublished(self):
        """Return unpublished announcements."""
        return self.filter(Q(publish_from__gt=now()) |
                           (Q(publish_until__isnull=False) &
                            Q(publish_until__lte=now())))
