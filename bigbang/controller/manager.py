from oslo_log import log as logging
from bigbang.api_route import wsgi

LOG = logging.getLogger(__name__)


class Manager(object):
    def get_all_person(self, context):
        LOG.info('get message from MQ')
        return {'message': "there is no person"}


class RouteManager(object):
    def get_all_person(self, request=None):
        LOG.info('get message from mapper&route')
        return {'message': "there is no person"}


def create_resource():
    """Images resource factory method"""
    # deserializer = ImageDeserializer()
    # serializer = ImageSerializer()
    func = lambda x: x
    return wsgi.Resource(RouteManager(), func)
