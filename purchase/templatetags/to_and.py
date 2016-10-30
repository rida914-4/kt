from django import template

register = template.Library()

@register.filter
def to_and(value):
    if value:
        value = value.replace("/", "-").split('-')
        value = value[2] + '-' + value[0] + '-' + value[1]
        print(value)
        return value
