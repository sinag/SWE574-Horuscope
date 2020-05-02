from django.db import models

from instance.models import Instance
from root import settings

"""
Comment model
"""


class Comment(models.Model):
    instance = models.ForeignKey(Instance, on_delete=models.PROTECT, blank=False, null=False, db_index=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default=settings.DEFAULT_ADMIN,
                                   blank=False, null=False, db_index=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    body = models.CharField(max_length=500, blank=False, null=False)
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"