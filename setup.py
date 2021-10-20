from setuptools import setup, find_packages
packages = find_packages()

setup(
	name='python-comcigan',
	version='1.0.4',
	description='Comcigan api for Python',
	long_description=open('./README.md').read(),
	long_description_content_type='text/markdown',
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
