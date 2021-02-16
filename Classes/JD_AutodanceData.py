from UAF.Classes.JD_AutodanceRecordingStructure import Object as JD_AutodanceRecordingStructure
from UAF.Classes.JD_AutodanceVideoStructure import Object as JD_AutodanceVideoStructure
class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "JD_AutodanceData"
		Data['recording_structure'] = JD_AutodanceRecordingStructure.Serialize(CSerializer,ifstream,jdVersion,sizeOf=True)
		Data['video_structure'] = JD_AutodanceVideoStructure.Serialize(CSerializer,ifstream,jdVersion,sizeOf=True)
		CSerializer.Path(ifstream,Data,"autodanceSoundPath",jdVersion=jdVersion)
		
		return Data