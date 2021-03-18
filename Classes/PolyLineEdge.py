class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False,flags=None):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "PolyLineEdge"
        CSerializer.Vector2(ifstream,Data,"POS")
        CSerializer.Vector2(ifstream,Data,"Scale")
        CSerializer.Vector2(ifstream,Data,"SwitchTexture")
        CSerializer.ENUM(ifstream,Data,"HoleMode")
		CSerializer.Vector2(ifstream,Data,"Vector")
        CSerializer.Vector2(ifstream,Data,"NormalizedVector")
        CSerializer.float32(ifstream,Data,"Length")
        CSerializer.StringID(ifstream,Data,"GameMaterial")
		
		return Data