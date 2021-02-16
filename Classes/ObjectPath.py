class Object:
	class Level:
		@staticmethod
		def Serialize(CSerializer,ifstream,sizeOf):
			Data = {}
			CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
			
			CSerializer.String8(ifstream,Data,"name")
			CSerializer.uint32(ifstream,Data,"parent")
			
			# post analyzation to determine the string form
			if Data['parent'] == 1:
				Data['name'] = '..'
			return Data['name']
	@staticmethod
	def Serialize(CSerializer,ifstream,sizeOf):
		Data = {"__class":"ObjectPath"}
		## this serializes the data into a python dict for later processing ##
		pathArray = []
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		
		for i in range(CSerializer.uint32(ifstream,raw=True)):
			pathArray.append(Object.Level.Serialize(CSerializer,ifstream,sizeOf))
		
		CSerializer.String8(ifstream,Data,"id")
		CSerializer.uint32(ifstream,Data,"NULL")
		
		pathArray.append(Data['id'])
		
		result = "|".join(pathArray)
		
		return result