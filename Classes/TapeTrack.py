class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {"__class":"TapeTrack"}
		CSerializer.sizeOf(ifstream) if sizeOf else CSerializer.NULL()
		CSerializer.uint32(ifstream,Data,'id',)
		CSerializer.String8(ifstream,Data,'name')
		return Data