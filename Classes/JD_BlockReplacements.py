from UAF.Classes.JD_BlockDescriptor import Object as JD_BlockDescriptor
class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "JD_BlockReplacements"
		Data['BaseBlock'] = JD_BlockDescriptor.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		CSerializer.CList("JD_BlockDescriptor",ifstream,Data,"AlternativeBlocks",jdVersion)
		
		return Data