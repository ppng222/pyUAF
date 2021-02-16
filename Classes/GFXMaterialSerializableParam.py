class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False,flags=None):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()	
		
		Data['__class'] = "GFXMaterialSerializableParam"
		CSerializer.float32(ifstream,Data,"Reflector_factor")
		
		return Data