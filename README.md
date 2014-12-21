flask-boilerplate-buildutils
=============

Configuration switching and build targets for flask-boilerplate.

Basic Usage
------------

This module simply exposes some helper classes for use within
the boilerplate. These include:

- StandardVirtualEnvTarget
- StandardMySQLDBTarget
- StandardSQLiteTarget
- StandardTestTarget


For further documentation of this package, see [readthedocs](http://flask-boilerplate-buildutils.readthedocs.org/en/latest/).


Advanced Target
-----------------

```
from maketools import Target

class MyOtherTarget(Target):
	# Define another target just to use it as a dependency. 
	pass

class MyTarget(Target):
	sh_build_commands = ('ls -la',
						 'mkdir test')
	depends = ('requirements.txt')
	output = 'myfile.txt'
	echo = True
	always_build = False
	depends = (MyOtherTarget, 'requirements.txt')

	def py_build_commands()
		print ("Do something in python")
```