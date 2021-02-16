from UAF.Classes.MaterialGraphicClip import Object as MaterialGraphicClip
from UAF.Classes.BezierCurveFloat import Object as BezierCurveFloat
class Object(MaterialGraphicClip):
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		## this serializes the data into a python dict for later processing ##
		Data = {}
		# serialize the base class first #
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data.update(MaterialGraphicClip.Serialize(CSerializer,ifstream,jdVersion,False))
		
		# serialize object specific data #
		Data['__class'] = "MaterialGraphicAlphaThresholdClip"
		Data['CurveA'] = BezierCurveFloat.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		
		return Data
		
		