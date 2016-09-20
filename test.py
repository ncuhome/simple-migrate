import unittest


class TestMigrate(unittest.TestCase):

    def test_basic(self):
        from flask import Flask
        from flask_script import Manager
        from simple_migrate import MigrateCommand
        app = Flask(__name__)
        manager = Manager(app)
        manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    unittest.main()
