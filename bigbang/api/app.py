from oslo_service import service

_launcher = None

def setup():
    pass

def serve(api_service, conf, workers):
    global _launcher
    if not _launcher:
        raise
        pass

    _launcher = service.launch(conf, api_service, workers=workers)


def wait():
    _launcher.wait()
