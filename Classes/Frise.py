class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "Frise"
		print("Frise")
		CSerializer.Color(ifstream,Data,"EventShowColorDst")
		
		return Data