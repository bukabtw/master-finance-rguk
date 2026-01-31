from django import template
from core.models import PageContent

register = template.Library()

@register.simple_tag
def get_content(key, default=''):
    try:
        content = PageContent.objects.get(key=key)
        return content.content
    except PageContent.DoesNotExist:
        return default
