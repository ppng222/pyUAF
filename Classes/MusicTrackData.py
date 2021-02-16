from UAF.Classes.MusicTrackStructure import Object as MusicTrackStructure
class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "MusicTrackData"
		Data['structure'] = MusicTrackStructure.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		CSerializer.Path(ifstream,Data,"path",jdVersion=jdVersion)
		# CSerializer.Path(ifstream,Data,"url",jdVersion=jdVersion) not used in oldgen
		
		return Data