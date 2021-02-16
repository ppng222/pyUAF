from UAF.Classes.Clip import Object as Clip
class Object(Clip):
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		## this serializes the data into a python dict for later processing ##
		# serialize the base class first #
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data.update(Clip.Serialize(CSerializer,ifstream,jdVersion,False))
		## this objects serialized data will now be read ##
		
		Data['__class'] = "SoundwichClip"
		CSerializer.String8(ifstream,Data,"SoundwichEvent")
		
		return Data