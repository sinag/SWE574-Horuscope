import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from activitystream.models import ActivityStream
from root import settings
from root.settings import SERVER_ADDRESS

"""
Community object model
"""


class Community(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default=settings.DEFAULT_ADMIN,
                               blank=False, null=False, db_index=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)
    city = models.CharField(max_length=100, blank=True, null=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "community"
        verbose_name_plural = "communities"


@receiver(post_save, sender=Community)
def create_community_activity(sender, instance, created, **kwargs):
    if created:
        ActivityStream.objects.create(data="{\"@context\": \"https://www.w3.org/ns/activitystreams\", \"summary\": \"" + instance.author.username + " "
                                       "created '" + instance.name + "' community\", \"type\": \"Create Community\", \"actor\": "
                                       "\"http://" + SERVER_ADDRESS + "/users/view/" + str(instance.author.id) + "\", \"object\": "
                                       "\"http://" + SERVER_ADDRESS + "/communities/" + str(instance.id) + "\", \"target\": "
                                       "\"http://" + SERVER_ADDRESS + "/users/view/" + str(instance.author.id) + "\", \"published\": \"" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\"}")
    else:
        ActivityStream.objects.create(data="{\"@context\": \"https://www.w3.org/ns/activitystreams\", \"summary\": \"" + instance.author.username + " "
                                       "updated '" + instance.name + "' community\", \"type\": \"Update Community\", \"actor\": "
                                       "\"http://" + SERVER_ADDRESS + "/users/view/" + str(instance.author.id) + "\", \"object\": "
                                       "\"http://" + SERVER_ADDRESS + "/communities/" + str(instance.id) + "\", \"target\": "
                                       "\"http://" + SERVER_ADDRESS + "/users/view/" + str(instance.author.id) + "\", \"published\": \"" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\"}")


@receiver(pre_delete, sender=Community)
def delete_community_activity(sender, instance, **kwargs):
    ActivityStream.objects.create(data="{\"@context\": \"https://www.w3.org/ns/activitystreams\", \"summary\": \"" + instance.author.username + " "
                                       "deleted '" + instance.name + "' community\", \"type\": \"Delete Community\", \"actor\": "
                                       "\"http://" + SERVER_ADDRESS + "/users/view/" + str(instance.author.id) + "\", \"object\": "
                                       "\"http://" + SERVER_ADDRESS + "/communities/" + str(instance.id) + "\", \"target\": "
                                       "\"http://" + SERVER_ADDRESS + "/users/view/" + str(instance.author.id) + "\", \"published\": \"" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\"}")
