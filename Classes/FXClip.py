from UAF.Classes.FXBaseClip import Object as FXBaseClip
class Object(FXBaseClip):
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		## this serializes the data into a python dict for later processing ##
		Data = {}
		# serialize the base class first #
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data.update(FXBaseClip.Serialize(CSerializer,ifstream,jdVersion,sizeOf))
		
		# serialize object specific data #
		Data['__class'] = "FXClip"
		CSerializer.uint32(ifstream,Data,"KillParticlesOnEnd")
		
		return Data
		
		