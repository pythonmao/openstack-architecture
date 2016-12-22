from pecan import expose
from oslo_config import cfg
from oslo_log import log as logging
import pecan

LOG = logging.getLogger(__name__)
CONF = cfg.CONF

class PersonController(object):
    @expose('json')
    def index(self):
        context = pecan.request.context
        persons = pecan.request.rpcapi.get_all_person()
        LOG.info('need add person')
        return persons
        # return {'message': 'Need add person'}