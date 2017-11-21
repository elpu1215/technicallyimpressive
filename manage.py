#!/usr/bin/env python
from flask_script import Manager, Shell

from app import create_app, db
from app.models import *

app = create_app("development")
manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post)

manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == "__main__":
    manager.run()