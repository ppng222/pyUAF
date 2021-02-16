class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "MusicSignature"
		CSerializer.int32(ifstream,Data,"marker")
		CSerializer.int32(ifstream,Data,"beats")
		return Data