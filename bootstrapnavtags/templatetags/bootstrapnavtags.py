from django import template
from django.template.base import TemplateSyntaxError


register = template.Library()


@register.tag
def navitem(parser, token):
    bits = token.split_contents()
    template_tag = bits[0]

    if len(bits) < 3:
        raise template.TemplateSyntaxError, "%r tag requires at least two argument" % template_tag

    try:
        label = parser.compile_filter(bits[1])
    except TemplateSyntaxError as exc:
        exc.args = (exc.args[0] + ".  The label argument has be be in single quotes.",)
        raise

    try:
        viewname = parser.compile_filter(bits[2])
    except TemplateSyntaxError as exc:
        exc.args = (exc.args[0] + ".  The url argument has be be in single quotes, like the url tag in Django 1.5.",)
        raise

    bits = bits[3:]

    return NavItemNode(label, viewname, bits)


class NavItemNode(template.Node):
    def __init__(self, label, viewname, args):
        self.label = label
        self.viewname = viewname
        self.args = args

    def render(self, context):
        return ''
