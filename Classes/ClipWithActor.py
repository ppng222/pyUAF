from UAF.Classes.Clip import Object as Clip
from UAF.Classes.ObjectPath import Object as ObjectPath
class Object(Clip):
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {"__class":"ClipWithActor"}
		## this serializes the data into a python dict for later processing ##
		# serialize the base class first #
		Data.update(Clip.Serialize(CSerializer,ifstream,jdVersion,False))
		## this objects serialized data will now be read ##
		CSerializer.CList("ObjectPath",ifstream,Data,"ActorPaths",jdVersion)
		if jdVersion == "new":
			CSerializer.CList_Struct("uint32",ifstream,Data,"ActorIndices")
		
		Data['__class'] = "ClipWithActor"
		
		# make sure all empty lists are removed #
		
		return Data