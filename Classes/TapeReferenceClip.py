from UAF.Classes.Clip import Object as Clip
class Object(Clip):
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		## this serializes the data into a python dict for later processing ##
		Data = {}
		# serialize the base class first #
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data.update(Clip.Serialize(CSerializer,ifstream,jdVersion,False))
		
		# serialize object specific data #
		Data['__class'] = "TapeReferenceClip"
		CSerializer.Path(ifstream,Data,"Path",jdVersion=jdVersion)
		CSerializer.sizeOf(ifstream,Data) # resovler dictionary
		CSerializer.uint32(ifstream,Data,"Loop")
		
		return Data