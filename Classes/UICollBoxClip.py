from UAF.Classes.ClipWithActor import Object as ClipWithActor
from UAF.Classes.BezierCurveFloat import Object as BezierCurveFloat
class Object(ClipWithActor):
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		## this serializes the data into a python dict for later processing ##
		Data = {"__class": "UICollBoxClip"}
		# serialize the base class first #
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data.update(ClipWithActor.Serialize(CSerializer,ifstream,jdVersion,False))
		
		# serialize object specific data #
		Data['__class'] = "UICollBoxClip"
		Data['CurveX'] = BezierCurveFloat.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		Data['CurveY'] = BezierCurveFloat.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		Data['CurveSizeX'] = BezierCurveFloat.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		Data['CurveSizeY'] = BezierCurveFloat.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		
		return Data