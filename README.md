# simple-migrate

### A simple database migrate tool for flask

This tool based on alembic to generate migration scripts and exec them,
it works well in many cases, but I can't guarantee the generated scripts
is 100% reliable, please make sure backup your database before exec upgrade.

通过alembic自动生成迁移脚本并执行，方便实用，但不保证生成的脚本100%可靠。
生产环境下一定要在数据已备份的情况下执行数据库迁移，避免出现意外。

## Install

    pip install simple-migrate


## Usage

manage.py
```
from sample_migrate import MigrateCommand
from flask_script import Manager

manager.add_command('db', MigrateCommand)
```

terminal
```
$ python manage.py db --help
usage: Perform database migrations

Perform database migrations

positional arguments:
  {status,upgrade}
    status          Get status of migration
    upgrade         Do database upgrade

optional arguments:
  -?, --help        show this help message and exit
```
