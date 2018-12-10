import os, shutil

for dirname in ['dist', 'build', 'Physica.egg-info']:
	if os.path.isdir(dirname):
		shutil.rmtree(dirname)

os.system('python setup.py sdist bdist_wheel')

os.system('python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*')