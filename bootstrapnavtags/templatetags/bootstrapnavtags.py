from django import template
from django.core.urlresolvers import NoReverseMatch, reverse
from django.template.base import kwarg_re, TemplateSyntaxError
from django.utils.encoding import smart_text


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

    args = []
    kwargs = {}
    if len(bits):
        for bit in bits:
            match = kwarg_re.match(bit)
            if not match:
                raise TemplateSyntaxError("Malformed arguments to url tag")
            name, value = match.groups()
            if name:
                kwargs[name] = parser.compile_filter(value)
            else:
                args.append(parser.compile_filter(value))

    return NavItemNode(label, viewname, args, kwargs)


class NavItemNode(template.Node):
    def __init__(self, label, viewname, args, kwargs):
        self.label = label
        self.viewname = viewname
        self.args = args
        self.kwargs = kwargs

    def render(self, context):
        args = [arg.resolve(context) for arg in self.args]
        kwargs = dict([(smart_text(k, 'ascii'), v.resolve(context)) for k, v in self.kwargs.items()])

        label = self.label.resolve(context)
        if not label:
            raise NoReverseMatch("'navitem' requires a non-empty first argument.")

        viewname = self.viewname.resolve(context)
        if not viewname:
            raise NoReverseMatch("'navitem' requires a non-empty second argument.")

        url = reverse(viewname, args=args, kwargs=kwargs, current_app=context.current_app)

        path = context['request'].path
        link = '<a href="%s">%s</a>' % (url, label)

        if url in path or url == path:
            return '<li class="active">%s</li>' % (link)
        return '<li>%s</li>' % (link)
