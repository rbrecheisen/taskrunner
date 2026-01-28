import sys
import os
from django.core.management import execute_from_command_line


def makemigrations():
    args = ['manage.py', 'makemigrations', *sys.argv[1:]]
    execute_from_command_line(args)


def migrate():
    args = ['manage.py', 'migrate', *sys.argv[1:]]
    execute_from_command_line(args)


def runserver():
    args = ['manage.py', 'runserver', *sys.argv[1:]]
    execute_from_command_line(args)


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taskrunner.settings")
    makemigrations()
    migrate()
    runserver()
    