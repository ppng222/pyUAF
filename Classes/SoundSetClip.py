from UAF.Classes.Clip import Object as Clip
from UAF.Classes.ClipWithActor import Object as ClipWithActor
class Object(Clip):
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		## this serializes the data into a python dict for later processing ##
		# serialize the base class first #
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		if jdVersion != "2014":
			Data.update(Clip.Serialize(CSerializer,ifstream,jdVersion,False))
		else:
			Data.update(ClipWithActor.Serialize(CSerializer,ifstream,jdVersion,False))
		## this objects serialized data will now be read ##
		
		Data['__class'] = "SoundSetClip"
		CSerializer.Path(ifstream,Data,"SoundSetPath")
		CSerializer.uint32(ifstream,Data,"SoundChannel")
		CSerializer.uint32(ifstream,Data,"StopsOnEnd")
		if jdVersion != "2014":
			CSerializer.uint32(ifstream,Data,"AccountedForDuration")
		return Data