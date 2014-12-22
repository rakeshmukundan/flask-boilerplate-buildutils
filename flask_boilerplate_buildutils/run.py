import os
import sys
def run_app(runfile='./run.py'):
	"""
	Helper to run the app. Serious hackery.
	"""
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
	Patches a command to use the virtualenvironment.
	"""
	return 'source ./.venv/bin/activate && unset __PYVENV_LAUNCHER__'\
		' && {command}'.format(command=command)