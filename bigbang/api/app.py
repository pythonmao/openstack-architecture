from oslo_config import cfg
from oslo_service import service
from pecan import configuration
from pecan import make_app

from bigbang.api import hooks

_launcher = None


def setup():
    config = {
        'server': {
            'host': cfg.CONF.api.bind_host,
            'port': cfg.CONF.api.bind_port,
        },
        'app': {
            'root': 'bigbang.api.controller.root.RootController',
            'modules': ['bigbang.api'],
            'errors': {
                400: '/error',
                '__force_dict__': True
            }
        }
    }

    pecan_config = configuration.conf_from_dict(config)
    app_hooks = [
        hooks.ContextHook(),
        hooks.NoExceptionTracebackHook(),
        hooks.RPCHook(),
    ]

    app = make_app(
        pecan_config.app.root,
        hooks=app_hooks,
        force_canonical=False,
        log=getattr(config, 'logging', {})
    )

    return app


def serve(api_service, conf, workers):
    global _launcher
    if _launcher:
        raise 'error'

    _launcher = service.launch(conf, api_service, workers=workers)


def wait():
    _launcher.wait()
