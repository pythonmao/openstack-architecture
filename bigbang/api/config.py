import sys
from oslo_config import cfg
from oslo_log import log as logging

LOG = logging.getLogger(__name__)

api_opts = [
    cfg.StrOpt('bind_host', default='0.0.0.0',
               help=("api server ip")),
    cfg.IntOpt('bind_port', default='8080',
               help=("port")),
    cfg.IntOpt('workers', default=1,
               help=("the number of workers"))
]


def init(args, **kwargs):
    api_config_group = cfg.OptGroup(name='api', title='bigbang api options')
    cfg.CONF.register_group(api_config_group)
    cfg.CONF.register_opts(api_opts, group=api_config_group)
    logging.register_options(cfg.CONF)

    cfg.CONF(args=args, project='bigbang', **kwargs)


def setup_logging():
    product_name = 'bigbang'
    logging.setup(cfg.CONF, product_name)
    LOG.info('logging enable!')
    LOG.debug('command line %s', " ".join(sys.argv))
