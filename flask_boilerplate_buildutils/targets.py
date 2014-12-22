from maketools import Target
from .run import patched_command
import os

class StandardVirtualEnvTarget(Target):
    """
    A target to install and configure a pip3 virtualenv and 
    install all the needed requirements.
    """
    always_build= False
    depends = ('requirements.txt',)
    output = './.venv/setup'
    sh_build_commands = (
        patched_command('pip3 install -r requirements.txt --upgrade'),
        )
    def py_build_commands(self):
        if os.system('which virtualenv'):
            raise Exception("Virtualenv not installed on your system. "\
                "Have you installed flask-boilerplate-buildutils?")

        if not os.path.exists('./.venv'):
            os.system('virtualenv ./.venv -p /usr/bin/python3',)


class StandardMySQLDBTarget(Target):
    """
    A target for use with a MySQL configuration. Performs required database 
    creation and dropping when needed.
    """
    echo = True

    sh_clean_commands = (
        'echo "DROP DATABASE IF EXISTS {DB_DATABASE};" | mysql -u {DB_USERNAME}',)
    
    sh_build_commands = (
        patched_command('pip3 install -r requirements-mysql.txt --upgrade'),
        'echo "CREATE DATABASE IF NOT EXISTS {DB_DATABASE}" | mysql -u {DB_USERNAME}',)

    depends = ('requirements-mysql.txt',)
    output = './.venv/db'


class StandardRegenerateTarget(Target):
    """
    A target to compile less files to css and do automatic imports for
    the python modules.
    """
    echo = False
    always_build = True
    depends = ('requirements.txt',)
    

    sh_build_commands = ('./util/compile.sh ./Application/static/css > /dev/null',
                         './util/regenerate.sh ./Application/models Model > /dev/null',
                         './util/regenerate.sh ./Application/views View > /dev/null')
    

class StandardSQLiteTarget(Target):
    """
    A target for use with an SQLite configuration class.
    """
    sh_clean_commands = ('rm -rf ./Application/{DB_BASE}.db',)


class StandardTestTarget(Target):
    """
    A target for use when performing tests.
    """
    depends = ()
