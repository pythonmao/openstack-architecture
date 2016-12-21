from pecan import expose
from oslo_config import cfg
from oslo_log import log as logging

LOG = logging.getLogger(__name__)
CONF = cfg.CONF

class PersonController(object):
    @expose('json')
    def index(self):
        LOG.info('need add person')
        return {'message': 'Need add person'}