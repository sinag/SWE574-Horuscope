from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from root import settings
from actstream import signals, action
from django.contrib.auth import get_user_model

"""
Community object model
"""


class Community(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default=1,
                               blank=False, null=False, db_index=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "community"
        verbose_name_plural = "communities"

def save_community(sender,instance,**kwargs):
    action.send(instance.author, verb="Created a new Community", description="deneme", action_object=instance)

post_save.connect(save_community, sender=Community)