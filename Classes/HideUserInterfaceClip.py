from UAF.Classes.GameplayEventClip import Object as GameplayEventClip
class Object(GameplayEventClip):
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		## this serializes the data into a python dict for later processing ##
		Data = {}
		# serialize the base class first #
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data.update(GameplayEventClip.Serialize(CSerializer,ifstream,jdVersion,False))
		
		# serialize object specific data #
		Data['__class'] = "HideUserInterfaceClip"
		Data['EventType'] = 18
		return Data