def includeme(config):
    """All of the route for the configuration to find."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route("home", "/")
