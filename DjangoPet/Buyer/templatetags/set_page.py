from django import template

register = template.Library()


@register.filter
def get_upper(obj):
    return obj.upper()


@register.filter
def get_four(obj):
    return obj[:4]

@register.filter
def set_url(obj, r_url):
    return obj.replace(r_url,'')
