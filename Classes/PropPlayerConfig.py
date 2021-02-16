class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "PropPlayerConfig"
		CSerializer.int32(ifstream,Data,"Index")
		CSerializer.CList_Struct("uint32",ifstream,Data,"ActiveProps")
		return Data