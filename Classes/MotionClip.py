from UAF.Classes.Clip import Object as Clip
class Object(Clip):
	class MotionPlatformSpecific:
		class Object:
			@staticmethod
			def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
				Data = {}
				Data['__class'] = "MotionPlatformSpecific"
				CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
				CSerializer.float32(ifstream,Data,"ScoreScale")
				CSerializer.float32(ifstream,Data,"ScoreSmoothing")
				CSerializer.float32(ifstream,Data,"ScoringMode")
				return Data
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		## this serializes the data into a python dict for later processing ##
		# serialize the base class first #
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data.update(Clip.Serialize(CSerializer,ifstream,jdVersion,False))
		## this objects serialized data will now be read ##
		
		Data['__class'] = "MotionClip"
		CSerializer.Path(ifstream,Data,"ClassifierPath",jdVersion=jdVersion)
		CSerializer.uint32(ifstream,Data,"GoldMove")
		CSerializer.uint32(ifstream,Data,"CoachId")
		CSerializer.uint32(ifstream,Data,"MoveType")
		CSerializer.Color(ifstream,Data,"Color",sizeOf=sizeOf)
		Data['MotionPlatformSpecifics'] = CSerializer.CDict(Object.MotionPlatformSpecific.Object.Serialize,"uint32",ifstream,jdVersion,CSerializer.PlatformIdToStr)
		return Data