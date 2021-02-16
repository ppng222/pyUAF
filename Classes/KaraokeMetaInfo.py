class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {"__class":"KaraokeMetaInfo"}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		CSerializer.uint32(ifstream,Data,'id',)
		CSerializer.uint32(ifstream,Data,'WindowSize')
		CSerializer.uint32(ifstream,Data,'WindowHop')
		CSerializer.float32(ifstream,Data,'RMSThreshold')
		CSerializer.float32(ifstream,Data,'RMSTendencyToIncrease')
		CSerializer.float32(ifstream,Data,'RMSTendencyToDecrease')
		CSerializer.float32(ifstream,Data,'YinPitchTreshold')
		CSerializer.float32(ifstream,Data,'PitchLowerBound')
		CSerializer.float32(ifstream,Data,'PitchUpperBound')
		CSerializer.int32(ifstream,Data,'HistorySpan')
		CSerializer.int32(ifstream,Data,'SlidingMeanWindowSize')
		CSerializer.float32(ifstream,Data,'SlidingMeanVariationThreshold')
		CSerializer.int32(ifstream,Data,'NoPitchScoring')
		CSerializer.int32(ifstream,Data,'GraphicsPitchMeanWindow')
		return Data