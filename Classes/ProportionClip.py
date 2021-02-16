from UAF.Classes.ClipWithActor import Object as ClipWithActor
from UAF.Classes.BezierCurveFloat import Object as BezierCurveFloat
class Object(ClipWithActor):
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		## this serializes the data into a python dict for later processing ##
		Data = {"__class": "ProportionClip"}
		# serialize the base class first #
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data.update(ClipWithActor.Serialize(CSerializer,ifstream,jdVersion,False))
		
		# serialize object specific data #
		CurveX = BezierCurveFloat.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		CurveY = BezierCurveFloat.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		
		Data['__class'] = "ProportionClip"
		Data['CurveX'] = CurveX
		Data['CurveY'] = CurveY
		
		return Data