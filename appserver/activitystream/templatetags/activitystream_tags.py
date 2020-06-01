from django.template import Library
import json
import timeago, datetime

register = Library()


@register.filter
def summary(object):
    json_data = json.loads(object)
    return json_data['summary']


@register.filter
def published(object):
    json_data = json.loads(object)
    return timeago.format(datetime.datetime.strptime(json_data['published'], "%Y-%m-%d %H:%M:%S"),
                          datetime.datetime.now())


@register.filter
def object(object):
    json_data = json.loads(object)
    return json_data['object']


@register.filter
def type(object):
    json_data = json.loads(object)
    return json_data['type']


@register.filter
def delete(object):
    json_data = json.loads(object)
    a = "Delete" in json_data['type']
    return "Delete" in json_data['type']
