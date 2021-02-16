class Object:
	ENUM_Pause_Level = {
		0: "WorldUpdateLayer_Gameplay",
		1: "WorldUpdateLayer_CutScene",
		2: "WorldUpdateLayer_Menu",
		3: "WorldUpdateLayer_TRC",
		4: "WorldUpdateLayer_",
		5: "WorldUpdateLayer_",
		6: "WorldUpdateLayer_None",
	}
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "SceneConfig"
		CSerializer.CList("GameModeParameters",ifstream,Data,"gameModeParametersList",jdVersion)
		CSerializer.ENUM(ifstream,Data,"Pause_Level")
		return Data