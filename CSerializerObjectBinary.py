import UAF.RegisterObjects as RegisterObjects
import sys
from importlib import import_module as ObjectImport
import struct
import os
class Vector:
	def __init__(self,VectorArray):
		vectorLen = len(VectorArray)
		if vectorLen == 3:
			self.vectorType = "Vector3"
		elif vectorLen == 2:
			self.vectorType = "Vector2"
		self.data = VectorArray
class Enum:
	def __init__(self,name,value):
		self.name = name
		self.value = value
BinaryReader = sys.modules['UAF.CSerializerObjectBinary']
PlatformIdToStr = {0:"PC",1:"X360",2:"PS3",3:"ORBIS",4:"CTR",5:"WII",6:"EMUWII",7:"VITA",8:"WIIU",9:"IPAD",0xA:"DURANGO",0xB:"NX",0xC:"GGP"}
PlatformStrToId = {"PC":0,"X360":1,"PS3":2,"ORBIS":3,"CTR":4,"WII":5,"EMUWII":6,"VITA":7,"WIIU":8,"IPAD":9,"DURANGO":0xA,"NX":0xB,"GGP":0xC}
def ClassCRC(ifstream):
	CRC = struct.unpack('>I',ifstream.read(0x4))[0]
	Class = RegisterObjects.FindClass(CRC)
	return Class

def NULL():
	pass
def uint32(ifstream,DataStructure=None,name=None,raw=False,jdVersion="new"):
	VAL = struct.unpack('>I',ifstream.read(0x4))[0]
	if raw:
		return VAL
	else:
		DataStructure[name] = VAL
def sizeOf(ifstream,DataStructure,name="__sizeOf"):
	pass
def int32(ifstream,DataStructure=None,name=None,raw=False,jdVersion="new"):
	VAL = struct.unpack('>i',ifstream.read(0x4))[0]
	if raw:
		return VAL
	else:
		DataStructure[name] = VAL
def float32(ifstream,DataStructure=None,name=None,raw=False,jdVersion="new"):
	VAL = round(struct.unpack('>f',ifstream.read(0x4))[0],6)
	if raw:
		return VAL
	else:
		DataStructure[name] = VAL
def Vector2(ifstream,DataStructure=None,name=None,raw=False,jdVersion="new"):
	VAL = round(struct.unpack('>f',ifstream.read(0x4))[0],6)
	VAL2 = round(struct.unpack('>f',ifstream.read(0x4))[0],6)
	if raw:
		return [VAL,VAL2]
	else:
		DataStructure[name] = Vector([VAL,VAL2])
def Vector3(ifstream,DataStructure=None,name=None,raw=False,jdVersion="new"):
	VAL = round(struct.unpack('>f',ifstream.read(0x4))[0],6)
	VAL2 = round(struct.unpack('>f',ifstream.read(0x4))[0],6)
	VAL3 = round(struct.unpack('>f',ifstream.read(0x4))[0],6)
	if raw:
		return [VAL,VAL2,VAL3]
	else:
		DataStructure[name] = Vector([VAL,VAL2,VAL3])
def Bool(ifstream,DataStructure=None,name=None,raw=False,jdVersion="new"):
	VAL = uint32(ifstream,raw=True)
	if raw:
		return VAL
	else:
		DataStructure[name] = VAL
def Color(ifstream,DataStructure=None,name=None,raw=False,sizeOf=False,jdVersion="new"):
	b = float32(ifstream,raw=True)
	g = float32(ifstream,raw=True)
	r = float32(ifstream,raw=True)
	a = float32(ifstream,raw=True)
	VAL = [a,r,g,b]
	if raw:
		return VAL
	else:
		DataStructure[name] = Vector(VAL)
def String8(ifstream,DataStructure=None,name=None,raw=False,jdVersion="new"):
	VAL = ifstream.read(struct.unpack('>I',ifstream.read(0x4))[0]).decode('utf-8')
	if raw:
		return VAL
	else:
		DataStructure[name] = VAL
def StringID(ifstream,DataStructure=None,name=None,raw=False,jdVersion="new"):
	VAL = uint32(ifstream,raw=True)
	if VAL == 0xFFFFFFFF:
		VAL = ""
	else:
		VAL = 'SERIALIZED:{0:x}'.format(int(VAL))
	if raw:
		return VAL
	else:
		DataStructure[name] = VAL
def Path(ifstream,DataStructure=None,name=None,raw=False,jdVersion="new"):
	PART1 = String8(ifstream,raw=True)
	PART2 = String8(ifstream,raw=True)
	CRC = uint32(ifstream,raw=True)
	FLAGS = uint32(ifstream,raw=True)
	if jdVersion == "2014":
		VAL = PART1+PART2
	else:
		VAL = PART2+PART1
	if raw:
		return VAL
	else:
		DataStructure[name] = VAL
def ENUM(ifstream,DataStructure=None,name=None,raw=False,jdVersion="new"):
	DataStructure[name] = Enum(name,int32(ifstream,raw=True))
def Volume(ifstream,DataStructure=None,name=None,raw=False,jdVersion="new"):
	Decibels = float32(ifstream,raw=True)
	if raw:
		return Decibels
	else:
		DataStructure[name] = Decibels
def Angle(ifstream,DataStructure=None,name=None,raw=False,jdVersion="new"):
	Value = float32(ifstream,raw=True)
	if raw:
		return Value
	else:
		DataStructure[name] = Value
def CDict_Struct(dataType,keyType,ifstream,jdVersion,DictionaryResolver=None):
	'''
	THIS IS FOR STRUCT FUNCTIONS, i know theres probably
	a better way to handle this other than making so many
	CList functions but idrk how to do this
	'''
	Data = {}
	for i in range(BinaryReader.uint32(ifstream,raw=True)):
		SerializedKey = getattr(BinaryReader,keyType)(ifstream,raw=True,jdVersion=jdVersion)
		SerializedData = getattr(BinaryReader,dataType)(ifstream,raw=True,jdVersion=jdVersion)
		if DictionaryResolver != None:
			KeyName = DictionaryResolver[SerializedKey]
		else:
			KeyName = SerializedKey
		Data[KeyName] = SerializedData
	return Data
def CDict(ClassObject,keyType,ifstream,jdVersion,DictionaryResolver=None):
	Data = {}
	for i in range(BinaryReader.uint32(ifstream,raw=True)):
		CSerializerObject = ClassObject
		
		SerializedKey = getattr(BinaryReader,keyType)(ifstream,raw=True,jdVersion=jdVersion)
		SerializedData = CSerializerObject(ifstream,jdVersion=jdVersion,raw=True,sizeOf=False)
		
		if DictionaryResolver != None:
			KeyName = DictionaryResolver[SerializedKey]
		else:
			KeyName = SerializedKey
		
		Data[KeyName] = SerializedData
	return Data
def CList_Struct(structType,ifstream,DataStructure,name,jdVersion="new"):
	'''
	THIS IS FOR STRUCT FUNCTIONS, i know theres probably
	a better way to handle this other than making so many
	CList functions but idrk how to do this
	'''
	returnArray = []
	for i in range(BinaryReader.uint32(ifstream,raw=True)):
		SerializedData = getattr(BinaryReader,structType)(ifstream,raw=True,jdVersion=jdVersion)
		returnArray.append(SerializedData)
	if len(returnArray) != 0:
		DataStructure[name] = returnArray
def CList(__class,ifstream,DataStructure,name,jdVersion="new",subObject=None):
	returnArray = []
	# determine the format first #
	for i in range(BinaryReader.uint32(ifstream,raw=True)):
		if subObject == None:
			CSerializerObject = getattr(ObjectImport('.{Class}'.format(Class=__class),'UAF.Classes'),"Object")
			SerializedData = CSerializerObject.Serialize(BinaryReader,ifstream,jdVersion)
			returnArray.append(SerializedData)
		else:
			# this is a subobject class #
			CSerializerObject = getattr(getattr(ObjectImport('.{Class}'.format(Class=__class),'UAF.Classes'),subObject),"Object")
			SerializedData = CSerializerObject.Serialize(BinaryReader,ifstream,jdVersion)
			returnArray.append(SerializedData)
	if len(returnArray) != 0:
		DataStructure[name] = returnArray
def CList_Factory(Factory,ifstream,DataStructure,name,jdVersion="new"):
	# lets get the list amount #
	returnArray = []
	for i in range(BinaryReader.uint32(ifstream,raw=True)):
		__class = ClassCRC(ifstream)
		CSerializerObject = getattr(ObjectImport('.{Class}'.format(Class=__class),'UAF.Classes'),"Object")
		SerializedData = CSerializerObject.Serialize(BinaryReader,ifstream,jdVersion,sizeOf=False)
		returnArray.append(SerializedData)
	if len(returnArray) != 0:
		DataStructure[name] = returnArray