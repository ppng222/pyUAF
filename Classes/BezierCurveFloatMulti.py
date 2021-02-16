from UAF.Classes.KeyFloat import Object as KeyFloat
class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		## this serializes the data into a python dict for later processing ##
		Data = {"__class": "BezierCurveFloatMulti"}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		
		# serialize object specific data #
		Data['Keys'] = []
		for i in range(CSerializer.uint32(ifstream,raw=True)):
			Data['Keys'].append(KeyFloat.Serialize(CSerializer,ifstream,jdVersion,sizeOf=True))
		
		
		return Data