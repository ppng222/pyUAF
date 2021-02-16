class Object:
	ENUM_playMode = {
		0: "PlayMode_PlayFirst",
		1: "PlayMode_Random",
		2: "PlayMode_RandomRememberLast",
		3: "PlayMode_RandomSequence",
		4: "PlayMode_Sequence",
		5: "PlayMode_Input_OBSOLETE",
		6: "PlayMode_Serie"
	}
	ENUM_filterType = {
		0: "FilterType_LowPass",
		1: "FilterType_HighPass",
		2: "FilterType_None",
		3: "FilterType_BandPass"
	}
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "SoundParams"
		CSerializer.uint32(ifstream,Data,"numChannels")
		CSerializer.uint32(ifstream,Data,"loop")
		CSerializer.ENUM(ifstream,Data,"playMode")
		CSerializer.StringID(ifstream,Data,"playModeInput")
		CSerializer.Volume(ifstream,Data,"randomVolMin")
		CSerializer.Volume(ifstream,Data,"randomVolMax")
		CSerializer.float32(ifstream,Data,"delay")
		CSerializer.float32(ifstream,Data,"randomDelay")
		CSerializer.float32(ifstream,Data,"randomPitchMin")
		CSerializer.float32(ifstream,Data,"randomPitchMax")
		CSerializer.float32(ifstream,Data,"fadeInTime")
		CSerializer.float32(ifstream,Data,"fadeOutTime")
		CSerializer.float32(ifstream,Data,"filterFrequency")
		CSerializer.ENUM(ifstream,Data,"filterType")
		CSerializer.uint32(ifstream,Data,"metronomeType")
		CSerializer.uint32(ifstream,Data,"playOnNext")
		CSerializer.int32(ifstream,Data,"playOnNextTransition")
		CSerializer.uint32(ifstream,Data,"transitionSampleOffset")
		CSerializer.CList("SoundModifier",ifstream,Data,"modifiers",jdVersion)
		
		return Data