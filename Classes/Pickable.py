class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False,flags=None):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "Pickable"
		CSerializer.float32(ifstream,Data,"RELATIVEZ")
		CSerializer.Vector2(ifstream,Data,"SCALE")
		CSerializer.int32(ifstream,Data,"xFLIPPED")
		CSerializer.String8(ifstream,Data,"USERFRIENDLY")
		if jdVersion == "new":
			CSerializer.StringID(ifstream,Data,"MARKER")
		CSerializer.Vector2(ifstream,Data,"POS2D")
		CSerializer.Angle(ifstream,Data,"ANGLE")
		CSerializer.Path(ifstream,Data,"INSTANCEDATAFILE")
		
		return Data