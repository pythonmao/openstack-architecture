import sys

from oslo_config import cfg
from oslo_log import log as logging

from oslo_service import wsgi
from bigbang.api import app
from bigbang.api import config as api_config

CONF = cfg.CONF
LOG = logging.getLogger('bigbang.api')


def main():
    api_config.init(sys.argv[1:])
    api_config.setup_logging()
    host = CONF.api.bind_host
    port = CONF.api.bind_port
    workers = CONF.api.workers
    application = app.setup()

    service = wsgi.Server(CONF, 'bigbang', application, host, port)
    app.serve(service, CONF, workers)

    app.wait()
