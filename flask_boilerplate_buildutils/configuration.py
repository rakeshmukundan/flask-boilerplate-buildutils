import os, sys, inspect
from .targets import StandardVirtualEnvTarget

class BaseConfiguration(object):
    """
    :var dependencies: A tuple containing maketools.Target objects.
                       Used when building dependencies for a config.
    """

    dependencies = (StandardVirtualEnvTarget,)

    @classmethod
    def diction(cls):
        """
        Get the class's variable so we can pass them to build when
        we build the targets
        """
        diction = {name: getattr(cls, name) for name in dir(cls) if not name.startswith('__') }
        return diction

    @classmethod
    def build_dependencies(cls):
        """
        Read the dependencies for this configuration class and 
        perform their build function. (Using maketools)
        """
        for TargetClass in cls.dependencies:
            target = TargetClass()
            target.build(format_dict=cls.diction())



def choose_config(config_module):
    """
    Configuration switching function.
    -c CONFIG_CLASS in argv or set an environment variable FLASK_CONFIG=CONFIG_CLASS
    to have the configuration loaded automatically.

    :param config_module: the module in which you have imported your 
                          configuration classes
                          ie, `choose_config(config_module=sys.modules[__name__])`
                          if you whish to choose a config class defined in the current
                          file.
    """
    if '-c' in sys.argv:
        class_name = sys.argv[sys.argv.index('-c') + 1]
    elif '--config' in sys.argv:
        class_name = sys.argv[sys.argv.index('--config') + 1]
    elif os.environ.get('FLASK_CONFIG'):
        class_name = os.environ.get('FLASK_CONFIG')
    else:
        class_name = 'Development'

    clsmembers = inspect.getmembers(config_module, inspect.isclass)
    clsmembers = dict(clsmembers)
    if class_name in clsmembers:
        cls = clsmembers[class_name]
        return cls

    raise Exception("Configuration class '%s' could not be found." % (class_name))

def make_keys():
    """
    Generate/open the security keys on the fly and return them in a dictionary
    """
    d = './config/'
    salt_file = os.path.realpath(os.path.join(d, './salt.key'))
    security_key_file = os.path.realpath(os.path.join(d, './security.key'))

    SECURITY_PASSWORD_SALT = None
    SECRET_KEY = None

    if os.path.isfile(salt_file):
        with open(salt_file, 'r') as f:
            SECURITY_PASSWORD_SALT = f.read().strip()
    else:
        import uuid
        with open(salt_file, 'w') as f:
            SECURITY_PASSWORD_SALT = "%s%s%s" % (uuid.uuid4().hex, uuid.uuid4().hex, uuid.uuid4().hex)
            f.write(SECURITY_PASSWORD_SALT)

    if os.path.isfile(security_key_file):
        with open(security_key_file, 'r') as f:
            SECRET_KEY = f.read().strip()
    else:
        import uuid
        with open(security_key_file, 'w') as f:
            SECRET_KEY = "%s%s%s" % (uuid.uuid4().hex, uuid.uuid4().hex, uuid.uuid4().hex)
            f.write(SECRET_KEY)

    return {'SECURITY_PASSWORD_SALT': SECURITY_PASSWORD_SALT,
            'SECRET_KEY': SECRET_KEY
            }
