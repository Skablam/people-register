from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand, upgrade
from people_register.models import *    # noqa
from people_register.extensions import register_extensions, db
from people_register.main import app
import subprocess
import os


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def init_db():
    db.create_all()
    upgrade()

@manager.command
def unittest(report=False):
    """Run unit tests"""

    if report:
        subprocess.call(["py.test", "--junitxml=test-output/unit-test-output.xml",
                         "--cov-report=html:test-output/unit-test-cov-report"])
    else:
        subprocess.call(["py.test"])


@manager.command
def integrationtest(report=False):
    """Run integration tests"""

    if report:
        subprocess.call(["py.test", "--junitxml=test-output/integration-test-output.xml",
                         "integration_tests"])
    else:
        subprocess.call(["py.test", "integration_tests"])


@manager.command
def runserver(port=9998):
    """Run the app using flask server"""

    os.environ["PYTHONUNBUFFERED"] = "yes"
    os.environ["LOG_LEVEL"] = "DEBUG"
    os.environ["COMMIT"] = "LOCAL"

    app.run(debug=True, port=int(port))

if __name__ == "__main__":
    manager.run()
