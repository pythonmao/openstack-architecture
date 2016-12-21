from pecan import expose
from pecan import route
from pecan import request

from bigbang.api.controller import base
from bigbang.api.controller import link
from bigbang.api.controller import types

from bigbang.api.controller.v1 import person as v1person
from bigbang.api.controller.v1 import book as v1book


class MediaType(base.APIBase):
    """A media type representation."""

    fields = {
        'base': {
            'validate': types.Text.validate
        },
        'type': {
            'validate': types.Text.validate
        },
    }


class V1(base.APIBase):
    """The representation of the version 1 of the API."""

    fields = {
        'id': {
            'validate': types.Text.validate
        },
        'media_types': {
            'validate': types.List(types.Custom(MediaType)).validate
        },
        'links': {
            'validate': types.List(types.Custom(link.Link)).validate
        },
        'services': {
            'validate': types.List(types.Custom(link.Link)).validate
        },
    }

    @staticmethod
    def convert():
        v1 = V1()
        v1.id = "v1"
        v1.links = [link.Link.make_link('self', request.host_url,
                                        'v1', '', bookmark=True),
                    link.Link.make_link('describedby',
                                        'http://docs.openstack.org',
                                        'developer/valence/dev',
                                        'api-spec-v1.html',
                                        bookmark=True, type='text/html')]
        v1.media_types = [MediaType(base='application/json',
                                    type='application/vnd.openstack.valence.v1+json')]
        v1.services = [link.Link.make_link('self', request.host_url,
                                           'services', ''),
                       link.Link.make_link('bookmark',
                                           request.host_url,
                                           'services', '',
                                           bookmark=True)]
        return v1


class V1Controller(object):
    @expose('json')
    def index(self):
        return V1.convert()


route(V1Controller, 'person', v1person.PersonController())
route(V1Controller, 'book', v1book.BookController())
