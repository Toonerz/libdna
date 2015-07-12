from pandac.PandaModules import *
from panda3d.core import *
from DNAInteractiveProp import DNAInteractiveProp

class DNAAnimBuilding(DNAInteractiveProp):
	def __init__(self):
		DNAInteractiveProp.__init__(self)
		self.anim = ''

	def setAnim(self, anim):
		self.anim = anim

	def getAnim(self):
		return self.anim