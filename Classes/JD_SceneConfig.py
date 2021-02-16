from UAF.Classes.SceneConfig import Object as SceneConfig
class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data.update(SceneConfig.Serialize(CSerializer,ifstream,jdVersion,sizeOf))
		Data['__class'] = "JD_SceneConfig"
		#CSerializer.String8(ifstream,Data,"name")
		return Data