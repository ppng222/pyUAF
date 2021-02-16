class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "JD_AutodanceRecordingStructure"
		CSerializer.CList("Record",ifstream,Data,"records",jdVersion=jdVersion)
		
		return Data