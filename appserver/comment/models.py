import datetime

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from activitystream.models import ActivityStream
from instance.models import Instance
from root import settings
from root.settings import SERVER_ADDRESS

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


@receiver(post_save, sender=Comment)
def create_activity(sender, instance, **kwargs):
    ActivityStream.objects.create(data="{\"@context\": \"https://www.w3.org/ns/activitystreams\", \"summary\": \"Sina "
                                       "created new comment under post '" + instance.instance.title() + "'\", \"type\": \"Create Comment\", \"actor\": "
                                       "\"http://" + SERVER_ADDRESS + "/users/view/" + str(instance.instance.author_id) + "\", \"object\": "
                                       "\"http://" + SERVER_ADDRESS + "/comments/" + str(instance.instance.id) + "\", \"target\": "
                                       "\"http://" + SERVER_ADDRESS + "/communities/" + str(instance.instance.datatype.community.id) + "\", \"published\": \"" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\"}")
    pass