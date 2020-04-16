from django import template
from datatype.models import DataType
from property.models import Property

register = template.Library()


@register.filter
def datatype_name(datatype__id):
    return DataType.objects.get(id=datatype__id).name


@register.filter
def datatype_id(property_id):
    return Property.objects.get(id=property_id).datatype.id


@register.filter
def datatype_generic(datatype__id):
    return DataType.objects.get(id=datatype__id).generic
