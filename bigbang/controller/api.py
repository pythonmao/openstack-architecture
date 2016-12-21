from bigbang.common import rpc_service


class API(rpc_service.API):
    def __init__(self, transport=None, context=None, topic=None):
        super(API, self).__init__(
            transport, context, topic=topic)

    def get_all_person(self):
        self._call('get_all_person')
