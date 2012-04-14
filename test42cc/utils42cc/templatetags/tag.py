from django import template
from django.core.urlresolvers import reverse

register = template.Library()


class GetUrl(template.Node):
    def __init__(self, obj_str):
        self.object = template.Variable(obj_str)

    def render(self, context):
        try:
            obj = self.object.resolve(context)
            url = reverse('admin:%s_%s_change' %
                (obj._meta.app_label, obj._meta.module_name),
                args=(obj.pk,))
            return url
        except:
            return ''


def edit_link(parser, token):
    """ generate url to admin edit pgae
    """
    try:
        tag_name, obj_str = token.split_contents()
    except ValueError:
        error = "%r tag requires only one argument" % token.contents.split()[0]
        raise template.TemplateSyntaxError, error
    return GetUrl(obj_str)

register.tag('edit_link', edit_link)
