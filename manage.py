import os
import argparse
import alembic.config

from alembic import command as alembic_command
from dotenv import load_dotenv
from bot import main

load_dotenv()

DB_NAME = os.environ.get('DB_NAME')
BOT_TOKEN = os.environ.get('BOT_TOKEN')

parser = argparse.ArgumentParser(description='My Telegram Bot For VisaMetrics')
parser.add_argument('command', help='The command to execute', choices=['run', 'makemigrations', 'migrate'])

args = parser.parse_args()
command = args.command

if command == 'run':
    main()

elif command == 'makemigrations':
    alembicArgs = [
        '--raiseerr',
        'revision',
        '--autogenerate',
        '-m',
        'message'
    ]
    alembic.config.main(argv=alembicArgs)

elif command == 'migrate':
    alembic_cfg = alembic.config.Config("alembic.ini")
    alembic_command.upgrade(alembic_cfg, "head")
