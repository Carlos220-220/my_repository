# from blueprint import app
from blueprint.course.models import db as course_db
from blueprint.user.models import db as user_db
#
#
# if __name__ == '__main__':
#     course_db.create_all()
#     user_db.create_all()
#     app.run("127.0.0.1", port=8000,debug=True, use_reloader=True)

from blueprint import create_app, db
from flask_script import Manager
from flask_script import Command
from flask_migrate import Migrate, MigrateCommand

app = create_app()
manager = Manager(app, course_db)

migrate = Migrate(app, course_db)
manager.add_command("db", MigrateCommand)


class Hello(Command):
    def run(self):
        print("hello")


class Runserver(Command):
    def run(self):
        app.run(host="127.0.0.1", port=8000, use_reloader=True)


manager.add_command("hello", Hello)
manager.add_command("runserver", Runserver)

if __name__ == '__main__':
    manager.run()
