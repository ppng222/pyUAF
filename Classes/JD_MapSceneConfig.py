from UAF.Classes.JD_SceneConfig import Object as JD_SceneConfig
class Object:
	ENUM_type = {
		0: "SceneConfigType_None",
		1: "SceneConfigType_Song",
		2: "SceneConfigType_UI"
	}
	ENUM_musicscore = {
		0: "MusicScoreType_Menu",
		1: "MusicScoreType_Menu",
		3: "MusicScoreType_Count"
	}
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		JD_SceneConfig.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		Data['__class'] = "JD_MapSceneConfig"
		CSerializer.ENUM(ifstream,Data,"type")
		CSerializer.ENUM(ifstream,Data,"musicscore")
		CSerializer.String8(ifstream,Data,"soundContext")
		CSerializer.int32(ifstream,Data,"hud")
		CSerializer.int32(ifstream,Data,"cursors")
		return Data