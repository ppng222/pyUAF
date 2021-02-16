from UAF.Classes.TapeCase_Component import Object as TapeCase_Component
class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False,flags=None):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data.update(TapeCase_Component.Serialize(CSerializer,ifstream,jdVersion,sizeOf,flags))
		Data['__class'] = "MasterTape"
		
		return Data