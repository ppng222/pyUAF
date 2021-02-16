class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "MusicSection"
		CSerializer.int32(ifstream,Data,"marker")
		CSerializer.int32(ifstream,Data,"sectionType")
		CSerializer.String8(ifstream,Data,"comment")
		return Data