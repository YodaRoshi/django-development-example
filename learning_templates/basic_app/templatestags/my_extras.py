from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, '')


# register.filter('cut', cut)
# the first argument is what you want call this filter, and the second is actuall function
