from django.db import models

from datatype.models import DataType
from property.models import Property
from root import settings

"""
Instance object model
"""


class Instance(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default=settings.DEFAULT_ADMIN,
                               blank=False, null=False, db_index=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_on = models.DateTimeField(auto_now_add=True, blank=False,
                                      null=False)  # ToDo - Auto update this on record update
    datatype = models.ForeignKey(DataType, on_delete=models.PROTECT, blank=False, null=False, db_index=True)

    def fields(self):
        return Property.objects.all().filter(datatype=self.datatype.id)

    def title(self):
        from textfield.models import TextField
        from property.models import Property
        title_property = Property.objects.filter(datatype_id=self.datatype_id).first()
        result = TextField.objects.filter(instance_id=self.id).filter(property_id=title_property.id).first()
        if result is not None:
            return result.value
        else:
            return ''

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "instance"
        verbose_name_plural = "instances"
