"""empty message

Revision ID: 202a25e5c734
Revises: 33004fcae5f7
Create Date: 2016-09-22 16:57:37.651425

"""

# revision identifiers, used by Alembic.
revision = '202a25e5c734'
down_revision = '33004fcae5f7'

from alembic import op, context
import sqlalchemy as sa
from flask import current_app


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('register',
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], )
    )

    # MANUALLY ADDED the line below to grant permissions for the user found in config variable APP_SQL_USERNAME on table person.
    context.execute("GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE event TO " + current_app.config.get('APP_SQL_USERNAME'))
    context.execute("GRANT USAGE, SELECT ON SEQUENCE event_id_seq TO " + current_app.config.get('APP_SQL_USERNAME'))

    context.execute("GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE register TO " + current_app.config.get('APP_SQL_USERNAME'))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('register')
    op.drop_table('event')
    ### end Alembic commands ###
