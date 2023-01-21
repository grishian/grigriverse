from flask import Flask

def create_app(config=None):
    app = Flask(__name__)

    app.debug = True

    do_register_blueprints(app)

    return app


def do_register_blueprints(flaskapp):
    from myapp.bp_general import bp_general
    from myapp.bp_tutorials import bp_tutorials

    flaskapp.register_blueprint(bp_general)
    flaskapp.register_blueprint(bp_tutorials)




