flask-boilerplate-buildutils
=============

Configuration switching and build targets for flask-boilerplate.

Basic Usage
------------

This module simply exposes some helper classes for use within
the boilerplate. These include:

- `flask_boilerplate_buildutils.targets.StandardVirtualEnvTarget`
- `flask_boilerplate_buildutils.targets.StandardMySQLDBTarget`
- `flask_boilerplate_buildutils.targets.StandardSQLiteTarget`
- `flask_boilerplate_buildutils.targets.StandardTestTarget`

It exposes the class `flask_boilerplate_buildutils.configuration.BaseConfiguration`, 
a Configuration base class for use within the flask-boilerplate.

### Other Functions
- `flask_boilerplate_buildutils.configuration.choose_config`
Configuration switching function. -c CONFIG_CLASS in argv or set an environment
variable FLASK_CONFIG=CONFIG_CLASS to have the configuration loaded automatically.


- `flask_boilerplate_buildutils.configuration.make_keys`
Generate/open the security keys on the fly and return them in a dictionary

For further documentation of this package, see 
[readthedocs](http://flask-boilerplate-buildutils.readthedocs.org/en/latest/).