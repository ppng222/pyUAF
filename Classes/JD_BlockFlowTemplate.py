class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "JD_BlockFlowTemplate"
		CSerializer.uint32(ifstream,Data,"isMashUp")
		CSerializer.uint32(ifstream,Data,"IsPartyMaster")
		CSerializer.CList("JD_BlockReplacements",ifstream,Data,"BlockDescriptorVector",jdVersion)
		#Data['selectedMaps'] = CSerializer.CList_Struct("String8",ifstream,jdVersion)
		
		return Data