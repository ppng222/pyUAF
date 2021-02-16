class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "PropEvent"
		CSerializer.float32(ifstream,Data,"StartTime")
		CSerializer.float32(ifstream,Data,"Duration")
		CSerializer.CList_Struct("uint32",ifstream,Data,"AssociatedProps")
		return Data