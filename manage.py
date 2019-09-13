import os, sys

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from src import create_app, db

"""
The MigrateCommand contains a set of migration commands such as
 
    init, migrate, upgrade
    
    e.g.: python manage.py db init
    
"""


env_name = os.getenv('FLASK_ENV')

if not env_name:
    print('FLASK_ENV not set:')
    print('options:\n  - development \n  - production')
    print('Examples:')
    print('macOS: export FLASK_ENV=development')
    print('Windows: set FLASK_ENV=development')
    sys.exit(1)

app = create_app(env_name)

migrate = Migrate(app=app, db=db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
