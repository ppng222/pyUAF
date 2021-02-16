class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "PleoComponent"
		CSerializer.Path(ifstream,Data,"video",jdVersion=jdVersion)
		CSerializer.String8(ifstream,Data,"channelID")
		return Data