from oslo_log import log as logging
from bigbang.common import rpc_service

LOG = logging.getLogger(__name__)

class API(rpc_service.API):
    def __init__(self, transport=None, context=None, topic=None):
        super(API, self).__init__(
            transport, context, topic='bigbang-controller')

    def get_all_person(self):
        LOG.info('send to MQ')
        return self._call('get_all_person')
        # return self._cast('get_all_person')
