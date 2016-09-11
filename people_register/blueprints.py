# Import every blueprint file
from people_register.views import general, people, register


def register_blueprints(app):
    """
    Adds all blueprint objects into the app.
    """
    app.register_blueprint(general.general)
    app.register_blueprint(register.register)
    app.register_blueprint(people.people, url_prefix="/people")

    # All done!
    app.logger.info("Blueprints registered")
