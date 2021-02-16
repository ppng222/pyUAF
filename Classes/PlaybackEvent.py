class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "PlaybackEvent"
		CSerializer.uint32(ifstream,Data,"ClipNumber")
		CSerializer.float32(ifstream,Data,"StartClip")
		CSerializer.float32(ifstream,Data,"StartTime")
		CSerializer.float32(ifstream,Data,"Duration")
		CSerializer.float32(ifstream,Data,"Speed")
		
		return Data