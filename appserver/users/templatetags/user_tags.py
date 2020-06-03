from django import template

from follow.models import Follow

register = template.Library()


@register.simple_tag(takes_context=True)
def is_followed_by_user(context, user_id):
    return Follow.objects.filter(source_id=context['request'].user.id).filter(target_id=user_id).count() > 0


@register.simple_tag(takes_context=True)
def get_follow_id(context, user_id):
    return Follow.objects.filter(source_id=context['request'].user.id).filter(target_id=user_id).first().id