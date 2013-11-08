#!/usr/bin/python

from distutils.core import Command, setup
import unittest

UNITTESTS = [
		"tests", 
	]

class TestCommand(Command):
	user_options = [ ]

	def initialize_options(self):
		pass

	def finalize_options(self):
		pass

	def run(self):
		suite = unittest.TestSuite()

		suite.addTests( 
			unittest.defaultTestLoader.loadTestsFromNames( 
								UNITTESTS ) )

		result = unittest.TextTestRunner(verbosity=2).run(suite)

setup(name='gps_tools',
	version='0.1',
	description='Asorted collection of tools for playing with GPS data in Python.',
	license='GPL',
	long_description=open("README").read(),
	author='Tomaz Solc',
	author_email='tomaz.solc@tablix.org',

	packages = ['gps_tools'],

	scripts = [ 'scripts/gps_log' ],

	provides = ['gps_tools'],

	cmdclass = { 'test': TestCommand }
)
