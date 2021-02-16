from UAF.Classes.JD_AutodanceData import Object as JD_AutodanceData
class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "JD_AutodanceComponent_Template"
		CSerializer.String8(ifstream,Data,"song")
		Data['autodanceData'] = JD_AutodanceData.Serialize(CSerializer,ifstream,jdVersion,sizeOf=True)
		
		return Data