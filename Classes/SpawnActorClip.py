from UAF.Classes.Clip import Object as Clip
from UAF.Classes.ObjectPath import Object as ObjectPath
class Object(Clip):
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		## this serializes the data into a python dict for later processing ##
		# serialize the base class first #
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data.update(Clip.Serialize(CSerializer,ifstream,jdVersion,False))
		## this objects serialized data will now be read ##
		
		Data['__class'] = "SpawnActorClip"
		CSerializer.Path(ifstream,Data,"ActorPath",jdVersion=jdVersion)
		CSerializer.String8(ifstream,Data,"ActorName")
		CSerializer.Vector3(ifstream,Data,"SpawnPosition")
		Data['ParentActor'] = ObjectPath.Serialize(CSerializer,ifstream,jdVersion,sizeOf=True)
		
		return Data