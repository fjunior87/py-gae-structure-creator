import unittest
import py_gae_structure_creator
import os

class GaeStructureCreatorTest(unittest.TestCase):
	
	
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
		
		self.assertTrue("app.yaml" in dirContent)
		self.assertTrue("templates" in dirContent)
		self.assertTrue("static" in dirContent)
		
		appYaml = """application: testapp
version: 1
api_version: 1
runtime: python

handlers:
- url: /static
  static_dir: static
- url: .*
  script: main.py"""
		
		
		with open(os.path.join(testdirpath, "app.yaml")) as file:
			fileContent = ""
			for line in file:
				fileContent += line
			self.assertEqual(fileContent, appYaml)
		
		
if __name__ == '__main__':
	unittest.main()