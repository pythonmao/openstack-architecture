import eventlet
eventlet.monkey_patch()
from oslo_config import cfg
from oslo_service import service as common_service
import sys

from bigbang.api_route import config
from bigbang.api_route import service
from bigbang.common.i18n import _


def main():
    # the configuration will be read into the cfg.CONF global data structure
    config.init(sys.argv[1:])
    if not cfg.CONF.config_file:
        sys.exit(_("ERROR: Unable to find configuration file via the default"
                   " search paths (~/.bigbang/, ~/, /etc/bigbang/, /etc/) and"
                   " the '--config-file' option!"))

    try:
        api_route = service.serve_wsgi(service.BigbangApiService)
        launcher = common_service.launch(cfg.CONF, api_route,
                                         workers=cfg.CONF.api_workers or None)
        launcher.wait()
    except KeyboardInterrupt:
        pass
    except RuntimeError as e:
        sys.exit(_("ERROR: %s") % e)


if __name__ == "__main__":
    main()
