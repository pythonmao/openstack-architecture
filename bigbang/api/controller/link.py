import pecan

from bigbang.api.controller import base
from bigbang.api.controller import types


def build_url(resource, resource_args, bookmark=False, base_url=None):
    if base_url is None:
        base_url = pecan.request.host_url

    template = '%(url)s/%(res)s' if bookmark else '%(url)s/v1/%(res)s'
    # FIXME(lucasagomes): I'm getting a 404 when doing a GET on
    # a nested resource that the URL ends with a  '/'.
    # https://groups.google.com/forum/#!topic/pecan-dev/QfSeviLg5qs
    template += '%(args)s' if resource_args.startswith('?') else '/%(args)s'
    return template % {'url': base_url, 'res': resource, 'args': resource_args}


class Link(base.APIBase):
    """A link representation."""

    fields = {
        'href': {
            'validate': types.Text.validate
        },
        'rel': {
            'validate': types.Text.validate
        },
        'type': {
            'validate': types.Text.validate
        },
    }

    @staticmethod
    def make_link(rel_name, url, resource, resource_args,
                  bookmark=False, type=None):
        href = build_url(resource, resource_args,
                         bookmark=bookmark, base_url=url)
        if type is None:
            return Link(href=href, rel=rel_name)
        else:
            return Link(href=href, rel=rel_name, type=type)
