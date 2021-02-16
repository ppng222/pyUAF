from UAF.Classes.MusicSignature import Object as MusicSignature
from UAF.Classes.MusicSection import Object as MusicSection
class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "MusicTrackStructure"
		CSerializer.CList_Struct("int32",ifstream,Data,"markers")
		CSerializer.CList("MusicSignature",ifstream,Data,"signatures")
		CSerializer.CList("MusicSection",ifstream,Data,"sections")
		CSerializer.int32(ifstream,Data,"startBeat")
		CSerializer.int32(ifstream,Data,"endBeat")
		CSerializer.float32(ifstream,Data,"videoStartTime")
		# so for some reason, oldgen just DOESNT have the preview data in musictrack
		# so we're just gonna create some defaults
		Data['previewEntry'] = 0
		Data['previewLoopStart'] = 0
		Data['previewLoopEnd'] = 0
		CSerializer.Volume(ifstream,Data,"volume")
		return Data