from django import template
from django.conf import settings

register = template.Library()

@register.filter
def message_icon(level):
    return settings.MESSAGE_ICONS.get(level)