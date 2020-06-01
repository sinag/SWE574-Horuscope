from django.db import models


class ActivityStream(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    data = models.TextField()

    class Meta:
        ordering = ['created']
        verbose_name = "activitystream"
        verbose_name_plural = "activitystreams"
