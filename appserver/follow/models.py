import datetime

from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from activitystream.models import ActivityStream
from root import settings
from root.settings import SERVER_ADDRESS

"""
Follow model
"""


class Follow(models.Model):
    source = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default=settings.DEFAULT_ADMIN, blank=False, null=False, db_index=True, related_name="follow_source")
    target = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default=settings.DEFAULT_ADMIN, blank=False, null=False, db_index=True, related_name="follow_target")
    created_on = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "follow"
        verbose_name_plural = "follows"


@receiver(post_save, sender=Follow)
def create_follow_activity(sender, instance, **kwargs):
    ActivityStream.objects.create(data="{\"@context\": \"https://www.w3.org/ns/activitystreams\", \"summary\": \"'" + instance.source.username + "' "
                                       "started following '" + instance.target.username + "'\", \"type\": \"Follow User\", \"actor\": "
                                       "\"http://" + SERVER_ADDRESS + "/users/view/" + str(instance.source.id) + "\", \"object\": "
                                       "\"http://" + SERVER_ADDRESS + "/users/view/" + str(instance.target.id) + "\", \"target\": "
                                       "\"http://" + SERVER_ADDRESS + "/users/view/" + str(instance.target.id) + "\", \"published\": \"" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\"}")


@receiver(pre_delete, sender=Follow)
def delete_follow_activity(sender, instance, **kwargs):
    ActivityStream.objects.create(data="{\"@context\": \"https://www.w3.org/ns/activitystreams\", \"summary\": \"'" + instance.source.username + "' "
                                       "stopped following '" + instance.target.username + "'\", \"type\": \"UnFollow User\", \"actor\": "
                                       "\"http://" + SERVER_ADDRESS + "/users/view/" + str(instance.source.id) + "\", \"object\": "
                                       "\"http://" + SERVER_ADDRESS + "/users/view/" + str(instance.target.id) + "\", \"target\": "
                                       "\"http://" + SERVER_ADDRESS + "/users/view/" + str(instance.target.id) + "\", \"published\": \"" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\"}")
