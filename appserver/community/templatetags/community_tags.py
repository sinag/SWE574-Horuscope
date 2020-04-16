from django import template
from community.models import Community
from datatype.models import DataType
from datetimefield.models import DateTimeField
from instance.models import Instance
from integerfield.models import IntegerField
from textfield.models import TextField

register = template.Library()

"""
Get subscription_id using community_id and user_id from context
"""


@register.filter
def subscription_id(community_id, user_id):
    return Community.objects.get(id=community_id).subscription_set.all().filter(user__id=user_id)[0].id


"""
Get subscription count by user using community_id and user_id from context
"""


@register.filter
def subscription_count_by_user(community_id, user_id):
    return Community.objects.get(id=community_id).subscription_set.all().filter(user__id=user_id).count()


"""
Get subscription count using community_id from context
"""


@register.filter
def subscription_count(community_id):
    return Community.objects.get(id=community_id).subscription_set.all().count()


"""
Get post count using datatype_id and community_id from context
"""


@register.filter
def post_count(community_id):
    return Instance.objects.filter(datatype_id__in=DataType.objects.all().filter(community_id=community_id)).count()


"""
Get post type count using community_id from context
"""


@register.filter
def posttype_count(community_id):
    return Community.objects.get(id=community_id).datatype_set.all().count()


"""
Get referenced object count using community_id from context
"""


@register.filter
def reference_count(community_id):  # Todo - add post count
    return Community.objects.get(id=community_id).subscription_set.all().count() + Community.objects.get(
        id=community_id).datatype_set.all().count()


"""
Get community owner using community_id from context
"""


@register.filter
def community_owner(community_id):
    return Community.objects.all().get(id=community_id).author


"""
Get community name using community_id from context
"""


@register.filter
def community_name(community_id):
    return Community.objects.all().get(id=community_id).name


"""
Get property value using instance_id, property_id and property_type from context
"""


@register.simple_tag
def property_value(instance_id, property_id, property_type):
    if property_type == 0 or property_type == 4 or property_type == 5 or property_type == 6 or property_type == 7 or property_type == 8 or property_type == 9:
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


"""
Convert field_type to html input type
"""


@register.filter
def field_type_to_input_type(field_type):
    result = "text"
    if field_type == 0:
        result = "text"
    if field_type == 1:
        result = "number"
    if field_type == 2:
        result = "datetime-local"
    if field_type == 4:
        result = "url"
    if field_type == 5:
        result = "url"
    if field_type == 6:
        result = "url"
    if field_type == 7:
        result = "email"
    if field_type == 8:
        result = "url"
    if field_type == 9:
        result = "text"
    return result
