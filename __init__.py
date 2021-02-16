from UAF.Classes.Tape import Object as Tape
from UAF.Classes.Actor_Template import Object as Actor_Template
from UAF.Classes.Scene import Object as Scene 
from UAF import RegisterObjects
from UAF import DictToXML
import xml.etree.ElementTree as ET
from xml.dom import minidom
import os
import sys
import json
class UAF:
	def __init__(self,mode,jdVersion,inPath,outFile):
		## initialize the entire object
		os.chdir(os.path.split(sys.modules['UAF'].__file__)[0])
		self.SerializeMode = mode
		self.jdVersion = jdVersion
		self.ObjectGroup = {}
		self.ObjectType = os.path.splitext(os.path.splitext(inPath)[0])[1].strip(".")
		self.XML_FORMATS = ['isc']
		self.JSON_FORMATS = ['isg','tpl','tape','dtape','ktape','msh']
		if mode == "serialFromBinary":
			inFileMode = 'rb'
			outFileMode = 'w'
			self.inFile = open(inPath,inFileMode)
			self.outFile = open(outFile,outFileMode)
		else:
			inFileMode = 'r'
			outFileMode = 'wb'
			if self.ObjectType in self.XML_FORMATS:
				self.inFile = open(inPath,inFileMode)
				self.outFile = open(outFile,outFileMode)
	def Serialize(self):
		# mode is serialFromBinary or serialToBinary
		# sizeOfFlag for serialization from binary to text
		# objectType -> isg, isc, tpl...
		# jdVersion == 2014, 2015, new
		## we need to set the sizeOf flag based on the objectType ##
		sizeOfTypes = ['isg','tpl','tape','dtape','ktape','msh']
		if self.ObjectType in sizeOfTypes:
			sizeOf = True
			self.sizeOf = True
		else:
			sizeOf = False
		# import the correct serializer #
		if self.SerializeMode == 'serialFromBinary':
			if sizeOf:
				import UAF.CSerializerObjectBinary_sizeOf as CSerializerObject
			else:
				import UAF.CSerializerObjectBinary as CSerializerObject
		elif self.SerializeMode == 'serialToBinary':
			if sizeOf:
				import UAF.CSerializerObjectBinaryWriter_sizeOf as CSerializerObject
			else:
				import UAF.CSerializerObjectBinaryWriter as CSerializerObject
		
		# now start the serialization process based on the file type #
		if self.ObjectType == 'tape' or self.ObjectType == 'dtape' or self.ObjectType == 'ktape':
			self.ObjectGroup = Tape.Serialize(CSerializerObject,self.inFile,self.jdVersion,sizeOf)
		elif self.ObjectType == 'tpl':
			self.ObjectGroup = Actor_Template.Serialize(CSerializerObject,self.inFile,self.jdVersion,sizeOf)
		elif self.ObjectType == 'isc':
			self.ObjectGroup = Scene.Serialize(CSerializerObject,self.inFile,self.jdVersion,sizeOf)
	def JSON_Serializer(self):
		self.outFile.write(json.dumps(self.ObjectGroup))
	def XML_Serializer(self):
		root = ET.Element("root")
		root.append(DictToXML.XMLSerializeObject(self.ObjectGroup))
		string = minidom.parseString(ET.tostring(root)).toprettyxml(encoding='ISO-8859-1',indent="	").decode()
		self.outFile.write(string)
	def Binary_Serializer(self):
		pass
	def SerializeImpl(self):
		self.Serialize()
		## this function takes the python dict, and transforms it into the specified format
		if self.SerializeMode == "serialFromBinary":
			if self.ObjectType in self.JSON_FORMATS:
				self.JSON_Serializer()
			else:
				self.XML_Serializer()
		else:
			# serialize mode is to binary ! #
			self.Binary_Serializer()