class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		Data['__class'] = "Actor_Template"
		CSerializer.uint32(ifstream,raw=True) ## always 1
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		CSerializer.uint32(ifstream,raw=True) ## __class
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		CSerializer.uint32(ifstream,raw=True) ## TAGS
		CSerializer.uint32(ifstream,Data,'WIP')
		CSerializer.uint32(ifstream,Data,'LOWUPDATE')
		CSerializer.uint32(ifstream,Data,'UPDATE_LAYER')
		CSerializer.uint32(ifstream,Data,'PROCEDURAL')
		CSerializer.uint32(ifstream,Data,'STARTPAUSED')
		CSerializer.uint32(ifstream,Data,'FORCEISENVIRONMENT')
		
		CSerializer.CList_Factory([],ifstream,Data,'COMPONENTS',jdVersion)
		
		return Data