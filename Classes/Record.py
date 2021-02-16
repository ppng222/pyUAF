class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "Record"
		CSerializer.float32(ifstream,Data,"Start")
		CSerializer.float32(ifstream,Data,"Duration")
		return Data