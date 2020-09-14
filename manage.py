from app import create_app
from flask_script import Manager, Server

# create app instance
app = create_app('production')

manager = Manager(app)
manager.add_command('server', Server)
