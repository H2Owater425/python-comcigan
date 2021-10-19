from setuptools import setup, find_packages
packages = find_packages()
print(packages)

setup(
	name='python-comcigan',
	version='1.0.1',
	description='Comcigan api for Python',
	author='H2Owater425',
	author_email='h2o@h2owr.xyz',
	url='https://github.com/H2Owater425/python-comcigan',
	license='MIT',
	packages=packages,
	classifiers=[
			"Programming Language :: Python :: 3",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
	],
	python_requires='>=3.7',
)
