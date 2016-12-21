from pecan import expose
from pecan import route
from pecan import request
from bigbang.api.controller import base
from bigbang.api.controller import types
from bigbang.api.controller import link

from bigbang.api.controller.v1 import controller as v1controller


class Version(base.APIBase):
    fields = {
        'id': {
            'validate': types.Text.validate
        },
        'link': {
            'validate': types.List(types.Custom(link.Link)).validate
        }
    }

    @staticmethod
    def convert(id):
        version = Version()
        version.id = id
        version.link = [link.Link.make_link('self', request.host_url,
                                            id, '', bookmark=True)]
        return version


class Root(base.APIBase):
    fields = {
        'id': {
            'validate': types.Text.validate
        },
        'description': {
            'validate': types.Text.validate
        },
        'versions': {
            'validate': types.List(types.Custom(Version)).validate
        },
        'default_version': {
            'validate': types.Custom(Version).validate
        },
    }

    @staticmethod
    def convert():
        root = Root()
        root.name = "OpenStack Valence API"
        root.description = ("Valence is an OpenStack project")
        root.versions = [Version.convert('v1')]
        root.default_version = Version.convert('v1')
        return root


class RootController(object):
    @expose('json')
    def index(self):
        return Root.convert()


route(RootController, 'v1', v1controller.V1Controller())
