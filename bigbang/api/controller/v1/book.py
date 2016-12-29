from pecan import expose
from oslo_config import cfg
from oslo_log import log as logging

LOG = logging.getLogger(__name__)
CONF = cfg.CONF


class BookController(object):
    @expose('json')
    def index(self):
        LOG.info('need add book')
        return {'message': 'Need add book'}
