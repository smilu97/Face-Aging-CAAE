

def register_all_blueprints(app):

	from .main import app as main

	app.register_blueprint(main)