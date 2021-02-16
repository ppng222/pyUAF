from UAF.Classes.Pickable import Object as Pickable
from UAF.Classes.Bind import Object as Bind
class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False,flags=None):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data.update(Pickable.Serialize(CSerializer,ifstream,jdVersion,sizeOf,flags))
		Data['__class'] = "Actor"
		CSerializer.Path(ifstream,Data,"LUA",jdVersion=jdVersion)
		CSerializer.CList("Bind",ifstream,Data,'parentBind',jdVersion)
		CSerializer.CList_Factory("COMPONENTS",ifstream,Data,'COMPONENTS',jdVersion)
		
		return Data