from django import template

register = template.Library()

@register.filter
def range_filter(value, arg):
    return range(value, arg)
