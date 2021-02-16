class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		## this serializes the data into a python dict for later processing ##
		Data = {"__class": "BezierCurveFloatLinear"}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		
		# serialize object specific data #
		CSerializer.Vector2(ifstream,Data,"ValueLeft")
		CSerializer.Vector2(ifstream,Data,"NormalLeftOut")
		CSerializer.Vector2(ifstream,Data,"ValueRight")
		CSerializer.Vector2(ifstream,Data,"NormalRightIn")
		
		return Data