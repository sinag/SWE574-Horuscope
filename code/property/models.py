from django.db import models

from root import settings

"""
Property object model
"""
class Property(models.Model):
    datatype = models.ForeignKey('datatype.DataType', on_delete=models.CASCADE, blank=False, null=False, db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default=settings.DEFAULT_ADMIN,
                               blank=False, null=False, db_index=True)
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    type_choices = [
        (0, 'Text'),
        (1, 'Number'),
        (2, 'Datetime'),
        # (3, 'Enumeration'),
        (4, 'Video'),
        (5, 'Audio'),
        (6, 'Image'),
        (7, 'Email'),
        (8, 'URL'),
        (9, 'Location'),
    ]
    generic_choices = [
        (0, 'Custom'),
        (1, 'Generic'),
    ]
    type = models.SmallIntegerField(blank=False,
                                    null=False, choices=type_choices)
    generic = models.BooleanField(db_index=True, choices=generic_choices)  # False = Custom, True = Generic
    required = models.BooleanField(db_index=True, blank=False, null=False)

    def __str__(self):
        return str(str(self.id) + '-' + self.name)

    class Meta:
        verbose_name = "property"
        verbose_name_plural = "properties"
