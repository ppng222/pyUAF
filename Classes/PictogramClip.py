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
		
		Data['__class'] = "PictogramClip"
		CSerializer.Path(ifstream,Data,"PictoPath",jdVersion=jdVersion)
		CSerializer.uint32(ifstream,Data,"CoachCount")
		
		return Data