class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False,flags=None):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "PolyPointList"
        CSerializer.CList("PolyLineEdge",ifstream,Data,"LocalPoints",jdVersion)
		CSerializer.uint32(ifstream,Data,"Loop")
		CSerializer.float32(ifstream,Data,"Length")
		return Data