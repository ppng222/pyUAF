class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "SceneConfigs"
		CSerializer.uint32(ifstream,Data,"activeSceneConfig")
		CSerializer.CList_Factory("SceneConfigs",ifstream,Data,"sceneConfigs",jdVersion)
		
		return Data