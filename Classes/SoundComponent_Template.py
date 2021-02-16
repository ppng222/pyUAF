class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "SoundComponent_Template"
		CSerializer.CList("SoundDescriptor_Template",ifstream,Data,"soundList",jdVersion)
		
		return Data