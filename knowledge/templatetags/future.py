from django.template import Library
from django.template.defaulttags import cycle as cycle_original

register = Library()


@register.simple_tag
def cycle(*args, **kwargs):
    ''' A stub to get SortableTabularInline to work '''
    return cycle_original(*args, **kwargs)

@register.simple_tag
def url(*args, **kwargs):
    return " "
