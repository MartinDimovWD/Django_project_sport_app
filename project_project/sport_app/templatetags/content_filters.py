from django.template import Library

register = Library()


@register.filter('capitalize_each_word')
def capitalize_each_word(str):
    return " ".join([x.capitalize() for x in str.split()])
