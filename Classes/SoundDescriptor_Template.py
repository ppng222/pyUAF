from UAF.Classes.SoundParams import Object as SoundParams
class Object:
	ENUM_limitMode = {
		0: "LimiterMode_RejectNew",
		1: "LimiterMode_StopOldest",
		2: "LimiterMode_StopLowestVolume",
		3: "LimiterMode_OnlyOnePlaying"
	}
	ENUM_serialPlayingMode = {
		0: "SoundDescriptor_Template::PlayOrdered",
		1: "SoundDescriptor_Template::PlayRandom",
		2: "SoundDescriptor_Template::PlayOrdered_RandomStart"
	}
	ENUM_serialStoppingMode = {
		0: "SoundDescriptor_Template::FinishCurrentSound",
		1: "SoundDescriptor_Template::StopImmediate"
	}
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		print()
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "SoundDescriptor_Template"
		CSerializer.StringID(ifstream,Data,"name")
		CSerializer.Volume(ifstream,Data,"volume")
		CSerializer.StringID(ifstream,Data,"category")
		CSerializer.StringID(ifstream,Data,"limitCategory")
		CSerializer.ENUM(ifstream,Data,"limitMode")
		CSerializer.uint32(ifstream,Data,"maxInstances")
		CSerializer.int32(ifstream,Data,"isStream")
		CSerializer.int32(ifstream,Data,"isPrefetched")
		CSerializer.CList_Struct("Path",ifstream,Data,"files",jdVersion)
		CSerializer.CList_Struct("Path",ifstream,Data,"filesIntro",jdVersion)
		CSerializer.CList_Struct("Path",ifstream,Data,"filesBody",jdVersion)
		CSerializer.CList_Struct("Path",ifstream,Data,"filesOutro",jdVersion)
		CSerializer.ENUM(ifstream,Data,"serialPlayingMode")
		CSerializer.ENUM(ifstream,Data,"serialStoppingMode")
		Data['params'] = SoundParams.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		CSerializer.uint32(ifstream,Data,"pauseInsensitiveFlags")
		CSerializer.uint32(ifstream,Data,"outDevices")
		CSerializer.uint32(ifstream,Data,"soundPlayAfterdestroy")
		
		return Data