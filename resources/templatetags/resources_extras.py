from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='replace')
@stringfilter
def replace(value, arg):
    return value.replace(arg, '')

@register.filter(name='custom')
@stringfilter
def custom(value, arg):
    arg = arg.upper()
    return "{0}: {1}".format(arg, value)