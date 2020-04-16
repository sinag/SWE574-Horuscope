from django.db import models
from community.models import Community
from property.models import Property
from root import settings

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
