.. flask-boilerplate-buildutils documentation master file, created by
   sphinx-quickstart on Sun Dec 21 20:36:38 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Flask Boilerplate Build Utils
========================================================

Requires pip module: maketools

.. toctree::
   :maxdepth: 2

flask_boilerplate_buildutils.configuration
--------------------------------------------------------

.. automodule:: flask_boilerplate_buildutils.configuration

.. autoclass:: BaseConfiguration
    :members: build_dependencies

.. autofunction:: choose_config

flask_boilerplate_buildutils.targets
--------------------------------------------------------
maketools helper targets for use with the boilerplate.

.. automodule:: flask_boilerplate_buildutils.targets

.. autoclass:: StandardVirtualEnvTarget
    :members:

.. autoclass:: StandardMySQLDBTarget
    :members:

.. autoclass:: StandardRegenerateTarget
    :members:

.. autoclass:: StandardSQLiteTarget
    :members:

.. autoclass:: StandardTestTarget
    :members:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

