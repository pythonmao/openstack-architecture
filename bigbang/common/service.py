# -*- encoding: utf-8 -*-
#
# Copyright © 2012 eNovance <licensing@enovance.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


from oslo_concurrency import processutils
from oslo_log import log
from oslo_service import service
from oslo_service import wsgi

from bigbang.api import app
from bigbang.common import config
from bigbang.common import exception
from bigbang.common.i18n import _
from oslo_config import cfg

CONF = cfg.CONF
LOG = log.getLogger(__name__)


def prepare_service(argv=None):
    if argv is None:
        argv = []
    log.register_options(CONF)
    config.parse_args(argv)
    config.set_config_defaults()
    log.setup(CONF, 'bigbang')
    # TODO(yuanying): Uncomment after objects are implemented
    # objects.register_all()


def process_launcher():
    return service.ProcessLauncher(CONF)


class WSGIService(service.ServiceBase):
    """Provides ability to launch Zun API from wsgi app."""

    def __init__(self, name, use_ssl=False):
        """Initialize, but do not start the WSGI server.

        :param name: The name of the WSGI server given to the loader.
        :param use_ssl: Wraps the socket in an SSL context if True.
        :returns: None
        """
        self.name = name
        self.app = app.load_app()
        self.workers = (CONF.api.workers or processutils.get_worker_count())
        if self.workers and self.workers < 1:
            raise exception.ConfigInvalid(
                _("api_workers value of %d is invalid, "
                  "must be greater than 0.") % self.workers)

        self.server = wsgi.Server(CONF, name, self.app,
                                  host=CONF.api.host,
                                  port=CONF.api.port,
                                  use_ssl=use_ssl)

    def start(self):
        """Start serving this service using loaded configuration.

        :returns: None
        """
        self.server.start()

    def stop(self):
        """Stop serving this API.

        :returns: None
        """
        self.server.stop()

    def wait(self):
        """Wait for the service to stop serving this API.

        :returns: None
        """
        self.server.wait()

    def reset(self):
        """Reset server greenpool size to default.

        :returns: None
        """
        self.server.reset()
