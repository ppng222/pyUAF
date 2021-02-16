class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		return {}