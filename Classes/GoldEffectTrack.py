from UAF.Classes.TapeTrack import Object as TapeTrack
class Object(TapeTrack):
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		## this serializes the data into a python dict for later processing ##
		Data = {}
		# serialize the base class first #
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data.update(TapeTrack.Serialize(CSerializer,ifstream,jdVersion,sizeOf))
		
		# serialize object specific data #
		
		Data['__class'] = "GoldEffectTrack"
		
		return Data