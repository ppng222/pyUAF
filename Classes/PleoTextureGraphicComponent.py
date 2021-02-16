from UAF.Classes.MaterialGraphicComponent import Object as MaterialGraphicComponent
class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data.update(MaterialGraphicComponent.Serialize(CSerializer,ifstream,jdVersion,sizeOf))
		Data['__class'] = "PleoTextureGraphicComponent"
		CSerializer.String8(ifstream,Data,"channelID")
		return Data