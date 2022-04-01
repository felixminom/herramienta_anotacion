from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.main import crear_aplicacion, db
from app import blueprint
from flask_cors import CORS
from os import getenv
from dotenv import load_dotenv

load_dotenv()

ENV = getenv('APP_ENV', 'dev')

app = crear_aplicacion(ENV)

app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

manager.add_command('db', MigrateCommand)

migrate = Migrate(app, db, compare_type=True)


CORS(app, resources='/*')

#Para ejecutar la aplicación corra el comando:
#python manage.py run
@manager.command
def run():
    app.run(port=5000,host='0.0.0.0')


if __name__ == '__main__':
    manager.run()
