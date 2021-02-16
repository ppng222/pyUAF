class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "AutodancePropData"
		CSerializer.int32(ifstream,Data,"Index")
		CSerializer.float32(ifstream,Data,"PivotX")
		CSerializer.float32(ifstream,Data,"PivotY")
		CSerializer.float32(ifstream,Data,"Size")
		CSerializer.float32(ifstream,Data,"fx_assetID")
		CSerializer.ENUM(ifstream,Data,"PropPart")
		
		return Data