from django import template


register = template.Library()

@register.filter
def diff(a, b):
    return abs(a-b)

