def register_routes(app):
    from .api import api
    from .main import main

    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(main)
