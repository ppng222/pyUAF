class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "GFX_Vector4"
		CSerializer.float32(ifstream,Data,"x")
		CSerializer.float32(ifstream,Data,"y")
		CSerializer.float32(ifstream,Data,"z")
		CSerializer.float32(ifstream,Data,"w")

		return Data