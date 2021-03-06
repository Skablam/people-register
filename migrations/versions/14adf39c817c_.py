"""empty message

Revision ID: 14adf39c817c
Revises: None
Create Date: 2016-09-25 22:37:25.064061

"""

# revision identifiers, used by Alembic.
revision = '14adf39c817c'
down_revision = None

from alembic import op, context
import sqlalchemy as sa
from flask import current_app


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('student', sa.Boolean(), nullable=True),
    sa.Column('member', sa.Boolean(), nullable=True),
    sa.Column('member_timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('entry',
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('level', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('person_id', 'event_id')
    )
    op.create_table('payment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    # MANUALLY ADDED the line below to grant permissions for the user found in config variable APP_SQL_USERNAME on table gadget.
    context.execute("GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE event TO " + current_app.config.get('APP_SQL_USERNAME'))
    context.execute("GRANT USAGE, SELECT ON SEQUENCE event_id_seq TO " + current_app.config.get('APP_SQL_USERNAME'))

    context.execute("GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE person TO " + current_app.config.get('APP_SQL_USERNAME'))
    context.execute("GRANT USAGE, SELECT ON SEQUENCE person_id_seq TO " + current_app.config.get('APP_SQL_USERNAME'))

    context.execute("GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE payment TO " + current_app.config.get('APP_SQL_USERNAME'))
    context.execute("GRANT USAGE, SELECT ON SEQUENCE payment_id_seq TO " + current_app.config.get('APP_SQL_USERNAME'))

    context.execute("GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE entry TO " + current_app.config.get('APP_SQL_USERNAME'))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payment')
    op.drop_table('entry')
    op.drop_table('person')
    op.drop_table('event')
    ### end Alembic commands ###
