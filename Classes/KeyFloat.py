class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		## this serializes the data into a python dict for later processing ##
		Data = {"__class": "KeyFloat"}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		
		# serialize object specific data #
		CSerializer.Vector2(ifstream,Data,"Value")
		CSerializer.Vector2(ifstream,Data,"NormalIn")
		CSerializer.Vector2(ifstream,Data,"NormalOut")
		return Data