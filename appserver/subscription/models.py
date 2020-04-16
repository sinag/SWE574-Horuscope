from django.db import models

from community.models import Community
from root import settings

"""
Subscription object model
"""


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=False, null=False, db_index=True)
    community = models.ForeignKey(Community, on_delete=models.PROTECT, blank=False, null=False, db_index=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "subscriptions"
