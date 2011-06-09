#!/usr/bin/env python
import os
from sys import argv
APP_YAML = "app.yaml"
TEMPLATES_DIR = "templates"
STATIC_DIR = "static"
MAIN_PY = "main.py"
class GaeStructureCreator:
	"""
	Class responsible to create an initial structure for GAE apps
	"""
	def __init__(self, appName):
		self.appName = appName
		
	def create(self):
		#currentDir = os.path.realpath(os.path.dirname(__file__))
		currentDir = os.getcwd()
		appDir = os.path.join(currentDir, self.appName)
		if not os.path.isdir(appDir):
			os.mkdir(appDir)
		
		with open(os.path.join(appDir,APP_YAML),"w") as app:
			app.write("application: %s\n" % self.appName)
			app.write("version: 1\n")
			app.write("api_version: 1\n")
			app.write("runtime: python\n")
			app.write("\n")
			app.write("handlers:\n")
			app.write("- url: /static\n")
			app.write("  static_dir: static\n")
			app.write("- url: .*\n")
			app.write("  script: main.py")
			
		with open(os.path.join(appDir,MAIN_PY), "w") as mainFile:
			pass

		
		self.createDir(appDir, TEMPLATES_DIR)
		self.createDir(appDir, STATIC_DIR)
	
	def createDir(self, appDir, newDir):
		"""
		Create a subdirectory given a parent dir path
		"""
		newDirPath = os.path.join(appDir, newDir)
		if not os.path.isdir(newDirPath):
			os.mkdir(newDirPath)
		
if __name__ == "__main__":
	if argv and len(argv) == 2:
		appName = argv[1]
		GaeStructureCreator(appName = appName).create()
	else:
		print "Please provide the appname\n"
		print "Usage:\n"
		print "py_gae_structure_creator.py appname"