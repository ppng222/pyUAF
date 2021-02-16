from UAF.Classes.GFXMaterialTexturePathSet import Object as GFXMaterialTexturePathSet
from UAF.Classes.GFXMaterialSerializableParam import Object as GFXMaterialSerializableParam
class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False,flags=None):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()	
		
		Data['__class'] = "GFXMaterialSerializable"
		Data['textureSet'] = GFXMaterialTexturePathSet.Serialize(CSerializer,ifstream,jdVersion,sizeOf,flags)
		CSerializer.uint32(ifstream,Data,"ATL_Channel")
		if jdVersion == "new":
			CSerializer.Path(ifstream,Data,"ATL_Path")
		CSerializer.Path(ifstream,Data,"shaderPath")
		Data['materialParams'] = GFXMaterialSerializableParam.Serialize(CSerializer,ifstream,jdVersion,sizeOf,flags)
		CSerializer.uint32(ifstream,Data,"stencilTest")
		CSerializer.uint32(ifstream,Data,"alphaTest")
		CSerializer.uint32(ifstream,Data,"alphaRef")
		
		return Data