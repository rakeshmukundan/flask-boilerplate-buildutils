import os
import sys
def run_app(runfile=None):
	"""
	Helper function to run the application in the current
	working directory.

	:param runfile: Specify a python file to be executed with a relative
					path. (default ./run.py)
	"""
	if (len(sys.argv) > 1) and not runfile:
		f = './{}.py'.format(sys.argv[1])
		if os.path.isfile(f):
			runfile = f
			sys.argv.pop(1)

	if not runfile:
		runfile = './run.py'

	os.system(patched_command(
		'python3 {runfile} {args}'.format(
			runfile=runfile,
			args=' '.join(
				list(map(lambda x: "'{arg}'".format(arg=x), sys.argv[1:]))
			)
		)
	))


def patched_command(command):
	"""
	Returns a patched shell command that will be executed inside
	the context of a virtual environment

	:param command: The command to be wrapped in the patching commands.
	"""
	return '/usr/bin/env bash -c "source ./.venv/bin/activate && unset __PYVENV_LAUNCHER__'\
		' && {command}"'.format(command=command)

def patch_cwd(filepath=None):
	"""
	Patch the current working directory to the caller's filepath.

	:param filepath: Set a filepath to become the current working
					 directory. If unspecified, the caller's __file__
					 path is used. 
	"""
	if not filepath:
		import inspect
		frame = inspect.stack()[1]
		module = inspect.getmodule(frame[0])
		filepath = module.__file__

	cwd = os.path.dirname(os.path.abspath(filepath))
	os.chdir(cwd)