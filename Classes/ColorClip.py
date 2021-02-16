from UAF.Classes.ClipWithActor import Object as ClipWithActor
from UAF.Classes.BezierCurveFloat import Object as BezierCurveFloat
class Object(ClipWithActor):
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		## this serializes the data into a python dict for later processing ##
		Data = {}
		# serialize the base class first #
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data.update(ClipWithActor.Serialize(CSerializer,ifstream,jdVersion,False))
		
		# serialize object specific data #
		CurveRed = BezierCurveFloat.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		CurveGreen = BezierCurveFloat.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		CurveBlue = BezierCurveFloat.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		
		Data['__class'] = "ColorClip"
		Data['CurveRed'] = CurveRed
		Data['CurveGreen'] = CurveGreen
		Data['CurveBlue'] = CurveBlue
		
		return Data