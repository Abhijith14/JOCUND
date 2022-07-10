from django import template


register = template.Library()


@register.filter(name='to_str')
def to_str(value):
    """converts int to string"""
    return str(value)
