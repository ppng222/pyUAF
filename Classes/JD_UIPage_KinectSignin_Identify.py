from UAF.Classes.JD_UIPage import Object as JD_UIPage
class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data.update(JD_UIPage.Serialize(CSerializer,ifstream,jdVersion,sizeOf))
		Data['__class'] = "JD_UIPage_KinectSignin_Identify"
		return Data