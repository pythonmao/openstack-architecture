from oslo_log import log as logging

LOG = logging.getLogger(__name__)


class Manager(object):
    def get_all_person(self, context):
        LOG.info('get message from MQ')
        return {'message': "there is no person"}
