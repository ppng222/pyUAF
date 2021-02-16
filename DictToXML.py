import xml.etree.ElementTree as ET
def listMap(value):
	## this allows the map function to turn Vector Arrays into strings for xml
	return "{:.6f}".format(value)
def tostring(XMLTREE):
	return ET.tostring(XMLTREE,encoding='ISO-8859-1')
def XMLSerializeObject(PyDICT):
	## this takes a dict and serializes it to XML
	xmlMainElement = ET.Element(PyDICT['__class'])
	for KEY in list(PyDICT):
		if KEY == '__class':
			continue
		if type(PyDICT[KEY]).__name__ == 'float':
			xmlMainElement.set(KEY,"{:.6f}".format(PyDICT[KEY]))
		elif type(PyDICT[KEY]).__name__ in ('int', 'long'):
			xmlMainElement.set(KEY,str(PyDICT[KEY]))
		elif type(PyDICT[KEY]).__name__ == 'Vector':
			xmlMainElement.set(KEY,' '.join(map(listMap,PyDICT[KEY].data)))
		elif type(PyDICT[KEY]).__name__ == "str":
			String = PyDICT[KEY].replace('\n','\x0A')
			xmlMainElement.set(KEY,String)
		elif type(PyDICT[KEY]).__name__ == 'dict':
			# we have to make a subobject under the root #
			subObject = ET.SubElement(xmlMainElement,KEY)
			serialData = XMLSerializeObject(PyDICT[KEY])
			subObject.append(serialData)
		elif type(PyDICT[KEY]).__name__ == 'list':
			for subKey in PyDICT[KEY]:
				subObject = ET.SubElement(xmlMainElement,KEY)
				subObject.set("NAME",subKey['__class'])
				serialData = XMLSerializeObject(subKey)
				subObject.append(serialData)
		elif type(PyDICT[KEY]).__name__ == 'Enum':
			subObject = ET.SubElement(xmlMainElement,"ENUM")
			subObject.set("NAME",PyDICT[KEY].name)
			subObject.set("SEL",str(PyDICT[KEY].value))
	return xmlMainElement
def XMLtoDict(FileHandle):
	'''
	so the function will receive a filehandle and it will read the entire thing and parse it
	'''
	assert type(FileHandle).__name__ == "TextIOWrapper", "THE FILE HANDLE IN XMLTODICT IS NOT A FILEHANDLE"
	XMLString = FileHandle.read()
	DictObject = {}
	# parse to xml tree 
	root = ET.fromstring(XMLString)
	