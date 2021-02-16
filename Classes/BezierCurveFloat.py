import UAF.RegisterObjects as RegisterObjects
from importlib import import_module as ObjectImport
from UAF.Classes.BezierCurveFloatEmpty import Object as BezierCurveFloatEmpty
from UAF.Classes.BezierCurveFloatConstant import Object as BezierCurveFloatConstant
from UAF.Classes.BezierCurveFloatLinear import Object as BezierCurveFloatLinear
from UAF.Classes.BezierCurveFloatMulti import Object as BezierCurveFloatMulti
class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		## this serializes the data into a python dict for later processing ##
		Data = {"__class": "BezierCurveFloat"}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		# serialize object specific data #
		CurveClass = RegisterObjects.FindClass(CSerializer.uint32(ifstream,raw=True))
		if CurveClass == "NULL":
			CurveClass = "BezierCurveFloatEmpty"
		BezierCurveHandler = getattr(ObjectImport('UAF.Classes.{Class}'.format(Class=CurveClass)),"Object")
		Data['Curve'] = BezierCurveHandler.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		return Data