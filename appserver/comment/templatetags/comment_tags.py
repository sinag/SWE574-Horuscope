from django import template
from datetimefield.models import DateTimeField
from integerfield.models import IntegerField
from textfield.models import TextField

register = template.Library()

"""
Get property value using instance_id, property_id and property_type from context
"""


@register.simple_tag
def property_value(instance_id, property_id, property_type):
    if property_type == 0 or property_type == 4 or property_type == 5 or property_type == 6 or property_type == 7 or property_type == 8 or property_type == 9 or property_type == 10:
        result = TextField.objects.filter(instance_id=instance_id).filter(property_id=property_id).first()
        if result is not None:
            return result.value
        else:
            return ''
    if property_type == 1:
        result = IntegerField.objects.filter(instance_id=instance_id).filter(property_id=property_id).first()
        if result is not None:
            if result.value is not None:
                return result.value
            else:
                return ''
        else:
            return ''
    if property_type == 2:
        result = DateTimeField.objects.filter(instance_id=instance_id).filter(property_id=property_id).first()
        if result is not None:
            if result.value is not None:
                return result.value.strftime("%Y-%m-%dT%H:%M:%S")
            else:
                return ''
        else:
            return ''

