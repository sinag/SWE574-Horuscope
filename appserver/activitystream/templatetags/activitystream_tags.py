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
    return "Delete" in json_data['type']


@register.filter
def icon(object):
    result = "fa-bell"
    json_data = json.loads(object)
    if "Community" in json_data["type"]:
        result = "fa-hashtag"
    if "DataType" in json_data["type"]:
        result = "fa-folder"
    if "Comment" in json_data["type"]:
        result = "fa-comments"
    if "Post" in json_data["type"]:
        result = "fa-comment-dots"
    if "Flag" in json_data["type"]:
        result = "fa-flag"
    return result
