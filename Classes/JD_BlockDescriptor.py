class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "JD_BlockDescriptor"
		CSerializer.String8(ifstream,Data,"songName")
		CSerializer.int32(ifstream,Data,"frstBeat")
		CSerializer.int32(ifstream,Data,"lastBeat")
		CSerializer.uint32(ifstream,Data,"songSwitch")
		CSerializer.Vector2(ifstream,Data,"videoCoachOffset")
		CSerializer.float32(ifstream,Data,"videoCoachScale")
		CSerializer.String8(ifstream,Data,"danceStepName")
		CSerializer.float32(ifstream,Data,"playingSpeed")
		CSerializer.uint32(ifstream,Data,"isEntryPoint")
		CSerializer.uint32(ifstream,Data,"isEmptyBlock")
		CSerializer.uint32(ifstream,Data,"isNoScoreBlock")
		CSerializer.String8(ifstream,Data,"guid")
		#CSerializer.uint32(ifstream,Data,"forceDisplayLastPictos")
		
		return Data