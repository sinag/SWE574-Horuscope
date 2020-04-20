from django import template

from subscription.models import Subscription
from flag.models import Flag

register = template.Library()

"""
Get community object from community id
"""


@register.simple_tag(takes_context=True)
def get_community_community_id(context):
    result = 0
    path = str(context['request'].path)
    if path.__contains__('communities') and not path.__contains__('update') and not path.__contains__(
            'delete') and not path.__contains__('create'):
        count = len(path.split('/'))
        if count == 4:
            result = path.split('/')[2]
    return result


"""
Check if current user subscribed to community from context.
"""


@register.simple_tag(takes_context=True)
def is_current_user_subscribed(context, community_id):
    result = False
    if Subscription.objects.filter(community_id=community_id).filter(user_id=context['request'].user.id).count() > 0:
        result = True
    return result

"""
Check if current user flagged a post before.
"""


@register.simple_tag(takes_context=True)
def is_flagged_by_user(context, instance_id):
    return Flag.objects.filter(instance_id=instance_id).filter(created_by_id=context['request'].user.id).count() > 0

@register.simple_tag(takes_context=True)
def get_flag_id_from_user_and_instance(context, instance_id):
    return Flag.objects.filter(instance_id=instance_id, created_by_id=context['request'].user.id).first().id

"""
Get datatype from community id
"""


@register.simple_tag(takes_context=True)
def get_datatype_community_id(context):
    result = 0
    path = str(context['request'].path)
    if path.__contains__('datatypes') and not path.__contains__('update') and not path.__contains__(
            'delete') and not path.__contains__('create'):
        count = len(path.split('/'))
        if count == 3:
            result = path.split('/')[2]
    return result
