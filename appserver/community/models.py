import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from activitystream.models import ActivityStream
from root import settings

"""
Community object model
"""


class Community(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default=settings.DEFAULT_ADMIN,
                               blank=False, null=False, db_index=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "community"
        verbose_name_plural = "communities"


@receiver(post_save, sender=Community)
def create_activity(sender, instance, **kwargs):
    ActivityStream.objects.create(data="{\"@context\": \"https://www.w3.org/ns/activitystreams\", \"summary\": \"Sina "
                                       "created '" + instance.name + "' community\", \"type\": \"Create Community\", \"actor\": "
                                       "\"http://127.0.0.1/users/view/"+ str(instance.author_id) +"\", \"object\": "
                                       "\"http://127.0.0.1/communities/" + str(instance.id) + "\", \"target\": "
                                       "\"http://127.0.0.1/users/view/"+ str(instance.author_id) +"\", \"published\": \"" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\"}")
    pass
