import os
import sys

from src import create_app

if __name__ == '__main__':
    env_name = os.getenv('FLASK_ENV')
    if not env_name:
        print('FLASK_ENV not set:')
        print('options:\n  - development \n  - production')
        print('Examples:')
        print('macOS: export FLASK_ENV=development')
        print('Windows: set FLASK_ENV=development')
        sys.exit(1)
    app = create_app(env_name)
    app.run()
