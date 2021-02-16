class Object:
	ENUM_allowCursors = {
		0: "CursorNone",
		1: "CursorFirstPlayer",
		2: "CursorAllPlayers",
		3: "CursorDRC",
		4: "CursorAllPlayersAndDRC",
		5: "CursorIgnore",
	}
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "JD_UIPage"
		CSerializer.ENUM(ifstream,Data,"allowCursors")
		CSerializer.uint32(ifstream,Data,"allowDPadNavigation")
		CSerializer.uint32(ifstream,Data,"hideBackButtonAtStart")
		CSerializer.uint32(ifstream,Data,"ShowUploadIcon")
		CSerializer.String8(ifstream,Data,"FirstWidgetDPad")
		CSerializer.uint32(ifstream,Data,"UNK")
		return Data