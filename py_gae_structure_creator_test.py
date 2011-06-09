import unittest
import py_gae_structure_creator
import os

class GaeStructureCreatorTest(unittest.TestCase):
	"""
	Unit Test Class for GaeStructureCreator class
	"""
	
	def setUp(self):
		self.appName = "testapp"
		dirname = os.path.join(os.path.realpath(os.path.dirname(__file__)), self.appName)
		if os.path.isdir(dirname):
			print "removing dir %s" % dirname
			import shutil
			shutil.rmtree(dirname)
	
	def tearDown(self):
		self.setUp()
	
	def test_create_app(self):
		gaeCreator = py_gae_structure_creator.GaeStructureCreator(appName = self.appName)
		gaeCreator.create()
		dirname = os.path.realpath(os.path.dirname(__file__))
		testdirpath = os.path.join(dirname,"testapp")
		self.assertTrue(os.path.exists(testdirpath))
		dirContent = os.listdir(testdirpath)
		
		self.assertTrue(py_gae_structure_creator.APP_YAML in dirContent)
		self.assertTrue(py_gae_structure_creator.TEMPLATES_DIR in dirContent)
		self.assertTrue(py_gae_structure_creator.STATIC_DIR in dirContent)
		self.assertTrue(py_gae_structure_creator.MAIN_PY in dirContent)
		
		 
		appYaml ="application: testapp\n"\
		"version: 1\n"\
		"api_version: 1\n"\
		"runtime: python\n"\
		"\n"\
		"handlers:\n"\
		"- url: /static\n"\
		"  static_dir: static\n"\
		"- url: .*\n"\
		"  script: main.py"\

		
		
		with open(os.path.join(testdirpath, "app.yaml")) as file:
			fileContent = ""
			for line in file:
				fileContent += line
			self.assertEqual(fileContent, appYaml)
		
		
if __name__ == '__main__':
	unittest.main()