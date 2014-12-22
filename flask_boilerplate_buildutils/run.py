import os
import sys
def run_app(runfile='./run.py'):
	"""
	Helper to run the app. Serious hackery.
	"""
	os.system('source ./.venv/bin/activate && unset '\
		'__PYVENV_LAUNCHER__ && python3 {runfile} {args}'.format(
			runfile=runfile,
			args=' '.join(list(map(lambda x: "'{arg}'".format(arg=x), sys.argv[1:])))
	))
