from UAF.Classes.MusicTrackData import Object as MusicTrackData
class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "MusicTrackComponent_Template"
		Data['trackData'] = MusicTrackData.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		
		return Data