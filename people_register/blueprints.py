# Import every blueprint file
from people_register.views import general, people, register, events


def register_blueprints(app):
    """
    Adds all blueprint objects into the app.
    """
    app.register_blueprint(general.general)
    app.register_blueprint(register.register)
    app.register_blueprint(people.people, url_prefix="/people")
    app.register_blueprint(events.events, url_prefix="/events")

    # All done!
    app.logger.info("Blueprints registered")
