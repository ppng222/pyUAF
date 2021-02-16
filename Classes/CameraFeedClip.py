from UAF.Classes.ClipWithActor import Object as ClipWithActor
class Object(ClipWithActor):
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		## this serializes the data into a python dict for later processing ##
		Data = {}
		# serialize the base class first #
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data.update(ClipWithActor.Serialize(CSerializer,ifstream,jdVersion,False))
		
		# serialize object specific data #
		Data['__class'] = "CameraFeedClip"
		CSerializer.uint32(ifstream,Data,"CaptureType")
		CSerializer.float32(ifstream,Data,"RecordBeat")
		CSerializer.uint32(ifstream,Data,"FeedType")
		
		return Data