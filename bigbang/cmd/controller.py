import sys
import os
from oslo_config import cfg
from oslo_log import log as logging
from oslo_service import service

from bigbang.common import service as bigbang_service
from bigbang.common import short_id
from bigbang.common import rpc_service
from bigbang.controller import manager

CONF = cfg.CONF
LOG = logging.getLogger(__name__)


def main():
    bigbang_service.prepare_service(sys.argv)

    LOG.info('Start controller server on PID %d', os.getpid())
    # CONF.log_opt_values(LOG, logging.DEBUG)

    controller_id = short_id.generate_id()
    endpoints = [
        manager.Manager(),
    ]

    server = rpc_service.Service.create('bigbang-controller', controller_id,
                                        endpoints, binary='bigbang-controller')
    launcher = service.launch(CONF, server)
    launcher.wait()