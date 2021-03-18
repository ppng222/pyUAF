class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False,flags=None):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()

		CSerializer.uint32(ifstream,Data,"allowBusMixEvents")
		CSerializer.uint32(ifstream,Data,"allowMusicEvents")
		
		
		Data['__class'] = "FXControllerComponent"
		

		return Data