from UAF.Classes.SceneConfigs import Object as SceneConfigs
class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "Scene"
		CSerializer.uint32(ifstream,raw=True) # 1
		CSerializer.uint32(ifstream,Data,"ENGINE_VERSION")
		CSerializer.CList_Struct("Path",ifstream,Data,"DEPENDENCIES",jdVersion)
		CSerializer.CList("Frise",ifstream,Data,"FRISE",jdVersion)
		CSerializer.CList("MetaFrieze",ifstream,Data,"METAFRIEZE",jdVersion)
		CSerializer.CList_Factory("ObjectFactory",ifstream,Data,"ACTORS",jdVersion)
		CSerializer.CList("FriezeConnectionResult",ifstream,Data,"friezeConnections",jdVersion)
		Data['sceneConfigs'] = SceneConfigs.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		if jdVersion != "2014":
			CSerializer.int32(ifstream,Data,"viewFamily")
		
		return Data