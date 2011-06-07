import os
from sys import argv
class GaeStructureCreator:
	appName = ""
	def __init__(self, appName):
		self.appName = appName
		
	def create(self):
		#currentDir = os.path.realpath(os.path.dirname(__file__))
		currentDir = os.getcwd()
		appDir = os.path.join(currentDir, self.appName)
		if not os.path.isdir(appDir):
			os.mkdir(appDir)
		
		with open(os.path.join(appDir,"app.yaml"),"w") as app:
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

		
		self.createDir(appDir, "templates")
		self.createDir(appDir, "static")
	
	def createDir(self, appDir, newDir):
		newDirPath = os.path.join(appDir, newDir)
		if not os.path.isdir(newDirPath):
			os.mkdir(newDirPath)
		
if __name__ == "__main__":
	if argv and len(argv) == 2:
		appName = argv[1]
		GaeStructureCreator(appName = appName).create()
	else:
		print "Please provide the appname"