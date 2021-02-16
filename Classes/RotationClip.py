from UAF.Classes.ClipWithActor import Object as ClipWithActor
from UAF.Classes.BezierCurveFloat import Object as BezierCurveFloat
class Object(ClipWithActor):
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		## this serializes the data into a python dict for later processing ##
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		# serialize the base class first #
		Data.update(ClipWithActor.Serialize(CSerializer,ifstream,jdVersion,False))
		
		# serialize object specific data #
		
		Data['__class'] = "RotationClip"
		Data['CurveX'] = BezierCurveFloat.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		Data['CurveY'] = BezierCurveFloat.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		Data['CurveZ'] = BezierCurveFloat.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		
		
		return Data