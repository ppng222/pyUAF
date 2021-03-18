from UAF.Classes.GraphicComponent import Object as GraphicComponent
class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False,flags=None):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()

		Data.update(GraphicComponent.Serialize(CSerializer,ifstream,jdVersion,sizeOf))
		
		Data['__class'] = "FXBankComponent"
		

		return Data