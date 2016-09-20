"""
A simple database migrate tool

This tool based on alembic to generate migration scripts and exec them,
it works well in many cases, but I can't guarantee the generated scripts
is 100% reliable, please make sure backup your database before exec upgrade.

通过alembic自动生成迁移脚本并执行，方便实用，但不保证生成的脚本100%可靠。
生产环境下一定要在数据已备份的情况下执行数据库迁移，避免出现意外。

Usage::

    # manage.py
    from sample_migrate import MigrateCommand
    from flask_script import Manager

    manager.add_command('db', MigrateCommand)

    # terminal
    $ python manage.py db --help
    usage: Perform database migrations

    Perform database migrations

    positional arguments:
      {status,upgrade}
        status          Get status of migration
        upgrade         Do database upgrade

    optional arguments:
      -?, --help        show this help message and exit
"""
import sqlalchemy as sa
from flask import current_app
from flask_script import Manager
from alembic.operations.base import Operations
from alembic.migration import MigrationContext
from alembic.autogenerate import produce_migrations
from alembic.autogenerate.api import AutogenContext
from alembic.autogenerate.render import render_op_text


MigrateCommand = Manager(usage='Perform database migrations')


@MigrateCommand.command
def status():
    """Get status of migration"""
    mc, lines = current_migration()
    if not lines:
        print("Already up-to-date.")
    else:
        print('-' * 79)
        print("\n".join(lines))
        print('-' * 79)
        print("Please review the code above then execute `upgrade` if OK.")


@MigrateCommand.command
def upgrade():
    """Do database upgrade"""
    mc, lines = current_migration()
    op = Operations(mc)
    if not lines:
        print("Already up-to-date.")
    else:
        print("Start Migration")
        print('-' * 79)
        with mc.begin_transaction():
            for line in lines:
                print(line)
                exec(line, {"sa": sa, "op": op})
        print('-' * 79)
        print("OK")


def current_migration():
    sqlalchemy = current_app.extensions['sqlalchemy']
    metadata, engine = sqlalchemy.db.metadata, sqlalchemy.db.engine
    return generate_migration(metadata, engine)


def generate_migration(metadata, engine):
    """Create MigrationContext and MigrationScript"""
    mc = MigrationContext.configure(engine.connect())
    ms = produce_migrations(mc, metadata)
    ac = AutogenContext(None, opts={
        'sqlalchemy_module_prefix': 'sa.',
        'alembic_module_prefix': 'op.',
    })
    lines = []
    for x in ms.upgrade_ops.ops:
        lines.append(render_op_text(ac, x))
    return mc, lines
