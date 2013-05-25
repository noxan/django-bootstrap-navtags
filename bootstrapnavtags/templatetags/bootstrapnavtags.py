from django import template


register = template.Library()


@register.tag
def navitem(parser, token):
    pass
