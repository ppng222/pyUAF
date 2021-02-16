from UAF.Classes.SizeClip import Object as SizeClip
from UAF.Classes.BezierCurveFloat import Object as BezierCurveFloat
class Object(SizeClip):
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		## this serializes the data into a python dict for later processing ##
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		# serialize the base class first #
		Data.update(SizeClip.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		Data['__class'] = "ScaleClip"
		return Data