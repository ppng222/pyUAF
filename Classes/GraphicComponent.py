from UAF.Classes.GFXPrimitiveParam import Object as GFXPrimitiveParam
class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False,flags=None):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "GraphicComponent"
		
		Data['PrimitiveParameters'] = GFXPrimitiveParam.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		CSerializer.uint32(ifstream,Data,"colorComputerTagId")
		CSerializer.uint32(ifstream,Data,"renderInTarget")
		CSerializer.uint32(ifstream,Data,"disableLight")
		CSerializer.uint32(ifstream,Data,"disableShadow")


		return Data