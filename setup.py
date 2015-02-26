import os
from setuptools import setup

readme_path = os.path.join(os.path.dirname(
  os.path.abspath(__file__)),
  'README.rst',
)
long_description = open(readme_path).read()
version_path = os.path.join(os.path.dirname(
  os.path.abspath(__file__)),
  'VERSION',
)
version = open(version_path).read()



setup(
  name='flask-boilerplate-buildutils',
  version=version,
  packages=['flask_boilerplate_buildutils'],
  author="Nick Whyte",
  author_email='nick@nickwhyte.com',
  description="Built utils for the flask-boilerplate/flask-boilerplate-utils",
  long_description=long_description,
  url='https://github.com/nickw444/flask-boilerplate-buildutils',
  include_package_data=True,
  zip_safe=False,
  install_requires=[
    'maketools',
    'virtualenv',
    'lesscpy'
  ],
  scripts=['flaskenv.sh']
)
