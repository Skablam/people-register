# Set the base image to the base image
FROM lr_base_python_flask

# ---- Database stuff start
RUN yum install -y -q postgresql-devel
ENV SQL_HOST postgres
# This must match the database created in postgres-init-fragment:
ENV SQL_DATABASE peopleregisterdb
# This is the root user specified in the postgres Dockerfile:
ENV ALEMBIC_SQL_USERNAME root
# (This will be temporarily overidden to yes when the alembic database upgrade is run)
ENV SQL_USE_ALEMBIC_USER no
# The following entries must match the user created in the fragments/postgres-init-fragment.sql:
ENV APP_SQL_USERNAME peopleuser
# (This will be temporarily overidden to be the root password when the alembic database upgrade is run)
ENV SQL_PASSWORD peoplepassword
# ---- Database stuff end
# ----
# Put your app-specific stuff here (extra yum installs etc).
# Any unique environment variables your config.py needs should also be added as ENV entries here

ENV APP_NAME people-register

# ----

# The command to run the app is inherited from lr_base_python_flask

# Get the python environment ready.
# Have this at the end so if the files change, all the other steps don't need to be rerun. Same reason why _test is
# first. This ensures the container always has just what is in the requirements files as it will rerun this in a
# clean image.
ADD requirements_test.txt requirements_test.txt
ADD requirements.txt requirements.txt
RUN pip3 install -q -r requirements.txt && \
  pip3 install -q -r requirements_test.txt
