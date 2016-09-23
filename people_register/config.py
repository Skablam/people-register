import os
# RULES OF CONFIG:
# 1. No region specific code. Regions are defined by setting the OS environment variables appropriately to build up the
# desired behaviour.
# 2. No use of defaults when getting OS environment variables. They must all be set to the required values prior to the
# app starting.
# 3. This is the only file in the app where os.getenv should be used.

# For logging
FLASK_LOG_LEVEL = os.getenv('LOG_LEVEL')

# For health route
COMMIT = os.getenv('COMMIT')

# This APP_NAME variable is to allow changing the app name when the app is running in a cluster. So that
# each app in the cluster will have a unique name.
APP_NAME = os.getenv('APP_NAME')

SQL_HOST = os.environ['SQL_HOST']
SQL_DATABASE = os.environ['SQL_DATABASE']
SQL_PASSWORD = os.environ['SQL_PASSWORD']
APP_SQL_USERNAME = os.environ['APP_SQL_USERNAME']
ALEMBIC_SQL_USERNAME = os.environ['ALEMBIC_SQL_USERNAME']

if os.getenv('SQL_USE_ALEMBIC_USER') == 'yes':
    FINAL_SQL_USERNAME = ALEMBIC_SQL_USERNAME
else:
    FINAL_SQL_USERNAME = APP_SQL_USERNAME

SQLALCHEMY_DATABASE_URI = 'postgres://{0}:{1}@{2}/{3}'.format(FINAL_SQL_USERNAME, SQL_PASSWORD, SQL_HOST, SQL_DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False  # Explicitly set this in order to remove warning on run

LOGCONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            '()': 'people_register.extensions.JsonFormatter'
        },
        'audit': {
            '()': 'people_register.extensions.JsonAuditFormatter'
        }
    },
    'filters': {
        'contextual': {
            '()': 'people_register.extensions.ContextualFilter'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'filters': ['contextual'],
            'stream': 'ext://sys.stdout'
        },
        'audit_console': {
            'class': 'logging.StreamHandler',
            'formatter': 'audit',
            'filters': ['contextual'],
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers': {
        'people_register': {
            'handlers': ['console'],
            'level': FLASK_LOG_LEVEL
        },
        'audit': {
            'handlers': ['audit_console'],
            'level': 'INFO'
        }
    }
}
