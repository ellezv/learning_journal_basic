from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include(".routes")
    # config.include(".views")
    config.scan()  # will find the decorator in views and add routes.
    return config.make_wsgi_app()
