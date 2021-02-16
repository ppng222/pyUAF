class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		## this serializes the data into a python dict for later processing ##
		Data = {"__class": "BezierCurveFloatConstant"}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		
		# serialize object specific data #
		CSerializer.float32(ifstream,Data,"Value")
		
		return Data