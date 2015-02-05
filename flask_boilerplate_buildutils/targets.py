from maketools import Target
from .run import patched_command
import os

class StandardVirtualEnvTarget(Target):
    """
    A target to install and configure a pip3 virtualenv and 
    install all the needed requirements.
    """
    always_build= False
    depends = ('./Application/requirements.txt',)
    output = './.venv/setup'
    sh_build_commands = (
        patched_command('pip3 install -r ./Application/requirements.txt --upgrade'),
        )
    def py_build_commands(self):
        if os.system('which virtualenv'):
            raise Exception("Virtualenv not installed on your system. "\
                "Have you installed flask-boilerplate-buildutils?")

        if not os.path.exists('./.venv'):
            os.system('virtualenv ./.venv -p `which python3.4`',)


class StandardMySQLDBTarget(Target):
    """
    A target for use with a MySQL configuration. Performs required database 
    creation and dropping when needed.
    """
    echo = True

    sh_clean_commands = (
        'echo "DROP DATABASE IF EXISTS {DB_DATABASE};" | mysql -u {DB_USERNAME}',)
    
    sh_build_commands = (
        patched_command('pip3 install -r ./Application/requirements-mysql.txt --upgrade'),
        'echo "CREATE DATABASE IF NOT EXISTS {DB_DATABASE}" | mysql -u {DB_USERNAME}',)

    depends = ('./Application/requirements-mysql.txt',)
    output = './.venv/db'

class StandardCIMySQLDBTarget(StandardMySQLDBTarget):
    """
    A target for use with CI. Same as MYSQL Target except has 
    a different output file so the CI Target gets made even
    if the MySQL target has been made
    """
    output = './.venv/ci'

class StandardRegenerateTarget(Target):
    """
    A target to compile less files to css and do automatic imports for
    the python modules.
    """
    echo = True
    always_build = True
    depends = ('requirements.txt',)
    

    sh_build_commands = (
        'lesscpy -X -m -V -r -o ./Application/static/css/  ./Application/static/css/',
        )
    
    def py_build_commands(self):
        folders_to_include = ['./Application/models', './Application/views']
        for folder in folders_to_include:
            names = []
            for root, dirs, files in os.walk(folder):
                with open(os.path.join(root, '__init__.py'), 'w') as fh:

                    for dir in dirs:
                        if not dir.startswith('_'):
                            # Recursively add folders. (BFS with a queue.)
                            module = os.path.join(root, dir)
                            folders_to_include.append(module)
                            # And import them recursively too.
                            fh.write('from .{module} import *\n'.format(module=os.path.basename(module)))
                    
                    for file in files:
                        if file.endswith('.py') and not file.startswith('_') and \
                            os.path.dirname(os.path.join(root,file)) == folder:
                            filename, ext = os.path.splitext(file)
                            names.append(filename)

                    for filename in sorted(names):
                        fh.write('from .{module} import {module}\n'.format(module=filename))



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
