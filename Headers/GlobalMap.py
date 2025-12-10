from collections import defaultdict
import os

class GlobalMap:
	def __init__(self):
		self.__Global_Map = defaultdict(str)

	def addPath( self, name, path ):
		name, path = name.strip(), path.strip()

		if path == '$':
			currentDir = os.getcwd()
			self.__Global_Map[ name ] = currentDir + os.sep
		else:
			self.__Global_Map[ name ] = path

	def getPath( self, name ):
		return self.__Global_Map.get( name, None )
