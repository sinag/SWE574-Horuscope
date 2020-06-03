import datetime

from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from activitystream.models import ActivityStream
from community.models import Community
from property.models import Property
from root import settings
from root.settings import SERVER_ADDRESS

"""
Datatype object model
"""


class DataType(models.Model):
    community = models.ForeignKey(Community, on_delete=models.PROTECT, blank=False, null=False, db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default=settings.DEFAULT_ADMIN,
                               blank=False, null=False, db_index=True)
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)
    generic_choices = [
        (0, 'Custom'),
        (1, 'Generic'),
    ]
    """
    For generic datatype generic = True
    For custom datatype generic = False
    """
    generic = models.BooleanField(db_index=True, choices=generic_choices)

    def __str__(self):
        return str(str(self.id) + '-' + self.name)

    def fields(self):
        """
        Returns fields inside this datatype
        """
        return Property.objects.all().filter(datatype=self.id)

    class Meta:
        verbose_name = "datatype"
        verbose_name_plural = "datatypes"


@receiver(post_save, sender=DataType)
def create_datatype_activity(sender, instance, created, **kwargs):
    if created:
        ActivityStream.objects.create(data="{\"@context\": \"https://www.w3.org/ns/activitystreams\", \"summary\": \"" + instance.author.username + " "
                                       "created '" + instance.name + "' post type under community '" + instance.community.name + "'\", \"type\": \"Create DataType\", \"actor\": "
                                       "\"http://" + SERVER_ADDRESS + "/users/view/" + str(instance.author_id) + "\", \"object\": "
                                       "\"http://" + SERVER_ADDRESS + "/properties/" + str(instance.id) + "\", \"target\": "
                                       "\"http://" + SERVER_ADDRESS + "/communities/" + str(instance.community.id) + "\", \"published\": \"" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\"}")
    else:
        ActivityStream.objects.create(data="{\"@context\": \"https://www.w3.org/ns/activitystreams\", \"summary\": \"" + instance.author.username + " "
                                       "updated '" + instance.name + "' post type under community '" + instance.community.name + "'\", \"type\": \"Update DataType\", \"actor\": "
                                       "\"http://" + SERVER_ADDRESS + "/users/view/" + str(instance.author_id) + "\", \"object\": "
                                       "\"http://" + SERVER_ADDRESS + "/properties/" + str(instance.id) + "\", \"target\": "
                                       "\"http://" + SERVER_ADDRESS + "/communities/" + str(instance.community.id) + "\", \"published\": \"" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\"}")


@receiver(pre_delete, sender=DataType)
def delete_datatype_activity(sender, instance, **kwargs):
    ActivityStream.objects.create(data="{\"@context\": \"https://www.w3.org/ns/activitystreams\", \"summary\": \"" + instance.author.username + " "
                                       "deleted '" + instance.name + "' post type under community '" + instance.community.name + "'\", \"type\": \"Delete DataType\", \"actor\": "
                                       "\"http://" + SERVER_ADDRESS + "/users/view/" + str(instance.author_id) + "\", \"object\": "
                                       "\"http://" + SERVER_ADDRESS + "/properties/" + str(instance.id) + "\", \"target\": "
                                       "\"http://" + SERVER_ADDRESS + "/communities/" + str(instance.community.id) + "\", \"published\": \"" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\"}")
