import struct
## these functions are for serialization of dicts

def sizeOf(ifstream):
	ifstream.read(0x4)
def NULL():
	pass
def uint32(ifstream,DataStructure=None,name=None,raw=False):
	VAL = struct.unpack('>I',ifstream.read(0x4))[0]
	if raw:
		return VAL
	else:
		DataStructure[name] = VAL
def int32(ifstream,DataStructure=None,name=None,raw=False):
	VAL = struct.unpack('>i',ifstream.read(0x4))[0]
	if raw:
		return VAL
	else:
		DataStructure[name] = VAL
def float32(ifstream,DataStructure=None,name=None,raw=False):
	VAL = round(struct.unpack('>f',ifstream.read(0x4))[0],6)
	if raw:
		return VAL
	else:
		DataStructure[name] = VAL
def Vector2(ifstream,DataStructure=None,name=None,raw=False):
	VAL = round(struct.unpack('>f',ifstream.read(0x4))[0],6)
	VAL2 = round(struct.unpack('>f',ifstream.read(0x4))[0],6)
	if raw:
		return [VAL,VAL2]
	else:
		DataStructure[name] = [VAL,VAL2]
def String8(ifstream,DataStructure=None,name=None,raw=False):
	VAL = ifstream.read(struct.unpack('>I',ifstream.read(0x4))[0])
	if raw:
		return VAL
	else:
		DataStructure[name] = VAL