class AudioPreview:
	class Object:
		@staticmethod
		def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
			Data = {}
			CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
			Data['__class'] = "AudioPreview"
			CSerializer.StringID(ifstream,Data,"name")
			CSerializer.int32(ifstream,Data,"startbeat")
			CSerializer.int32(ifstream,Data,"endbeat")
			return Data
class GameModeDesc:
	class Object:
		SongGameMode = {
			0: "SongGameMode_Classic",
			1: "SongGameMode_Mashup",
			2: "SongGameMode_PartyMaster",
			3: "SongGameMode_Sweat",
			4: "SongGameMode_Battle",
			5: "SongGameMode_OnStage",
			6: "SongGameMode_Max"
		}
		SongGameModeStatus = {
			0: "SGM_Status_Unavailable",
			1: "SGM_Status_Hidden",
			2: "SGM_Status_Locked",
			3: "SGM_Status_Available",
			4: "SGM_Status_RedeemLocked",
			5: "SGM_Status_UplayLocked",
			6: "SGM_Status_JDMLocked",
			7: "SGM_Status_AAAMapLocked",
			8: "SGM_Status_",
			9: "SGM_Status_GachaLocked",
			10: "SGM_Status_",
			11: "SGM_Status_DlcLocked",
			12: "SGM_Status_ObjectiveLocked",
			13: "SGM_Status_AnthologyLocked"
		}
		@staticmethod
		def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
			Data = {}
			CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
			Data['__class'] = "GameModeDesc"
			CSerializer.ENUM(ifstream,Data,"Mode")
			CSerializer.uint32(ifstream,Data,"SubFlags")
			if jdVersion != "2014":
				CSerializer.int32(ifstream,Data,"INT1")
				CSerializer.uint32(ifstream,Data,"LocaleID")
			CSerializer.ENUM(ifstream,Data,"Status")
			CSerializer.uint32(ifstream,Data,"MojoValue")
			Data['Colors'] = CSerializer.CDict(CSerializer.Color,"StringID",ifstream,jdVersion)
			CSerializer.Path(ifstream,Data,"ConfigTemplate",jdVersion=jdVersion)
			CSerializer.int32(ifstream,Data,"CountInProgression")
			return Data
class Object:
	StringIDResolver_AudioPreview = {
		"SERIALIZED:6f4037d0": "coverflow",
		"SERIALIZED:b11fc1b6": "prelobby"
	}
	StringIDResolver_DefaultColors = {
		"SERIALIZED:31d3b347": "lyrics",
		"SERIALIZED:9cd90bcb": "theme",
		"SERIALIZED:24a808d7": "songcolor_2a",
		"SERIALIZED:be0b9923": "songcolor_2b",
		"SERIALIZED:a292c8c4": "songcolor_1a",
		"SERIALIZED:f5825c67": "songcolor_1b"
	}
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "JD_SongDescTemplate"
		CSerializer.String8(ifstream,Data,"MapName")
		CSerializer.int32(ifstream,Data,"JDVersion")
		if jdVersion != '2014':
			CSerializer.int32(ifstream,Data,"OriginalJDVersion")
		CSerializer.CList_Struct("String8",ifstream,Data,"RelatedAlbums",jdVersion)
		CSerializer.CList("JD_SongDescTemplate",ifstream,Data,"GameModules",jdVersion,"GameModeDesc")
		CSerializer.String8(ifstream,Data,"Artist")
		if jdVersion != "2014":
			CSerializer.String8(ifstream,Data,"DancerName")
		CSerializer.String8(ifstream,Data,"Title")
		CSerializer.ENUM(ifstream,Data,"NumCoach")
		if jdVersion != "2014":
			CSerializer.ENUM(ifstream,Data,"MainCoach")
		CSerializer.ENUM(ifstream,Data,"Difficulty")
		if jdVersion != "2014":
			CSerializer.ENUM(ifstream,Data,"backgroundType")
			CSerializer.ENUM(ifstream,Data,"LyricsType")
		CSerializer.ENUM(ifstream,Data,"Energy")
		
		CSerializer.float32(ifstream,Data,"AudioPreviewFadeTime")
		CSerializer.CList("JD_SongDescTemplate",ifstream,Data,"AudioPreviews",jdVersion,subObject="AudioPreview")
		
		Data['DefaultColors'] = CSerializer.CDict(CSerializer.Color,"StringID",ifstream,jdVersion,Object.StringIDResolver_DefaultColors)
		Data['Paths'] = {}
		CSerializer.CList_Struct("Path",ifstream,Data['Paths'],"Avatars",jdVersion)
		if jdVersion != "2014":
			CSerializer.CList_Struct("Path",ifstream,Data['Paths'],"AsyncPlayers",jdVersion)
		Object.PostSerialize(Data,jdVersion)
		
		return Data
	@staticmethod
	def PostSerialize(Data,jdVersion):
		# this method will manage the dict after reading it
		# lets try to return stringids in audiopreview back to their original names if found
		for i in range(len(Data['AudioPreviews'])):
			Data['AudioPreviews'][i]['name'] = Object.StringIDResolver_AudioPreview[Data['AudioPreviews'][i]['name']]
		try:
			if len(Data['Paths']['Avatars']) == 0:
				Data['Paths']['Avatars'] = None
		except KeyError:
			Data['Paths']['Avatars'] = None
		if jdVersion != "2014":
			if len(Data['Paths']['AsyncPlayers']) == 0:
				Data['Paths']['AsyncPlayers'] = None
		
		
		
		