from UAF.Classes.ObjectPath import Object as ObjectPath
class Object:
	ENUM_type = {
		0: "Root",
		1: "BoneName",
		2: "ProceduralBoneName"
	}
	ENUM_scaleInheritProp = {
		0: "PropInherit_UseParent",
		1: "PropInherit_UseChild",
		2: "PropInherit_Combine"
	}
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False,flags=None):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "Bind"
		Data['parentPath'] = ObjectPath.Serialize(CSerializer,ifstream,sizeOf)
		CSerializer.ENUM(ifstream,Data,"type")
		CSerializer.uint32(ifstream,Data,"typeData")
		CSerializer.Vector3(ifstream,Data,"offsetPos")
		CSerializer.Angle(ifstream,Data,"offsetAngle")
		CSerializer.Vector2(ifstream,Data,"localScale")
		CSerializer.Bool(ifstream,Data,"useParentFlip")
		CSerializer.ENUM(ifstream,Data,"scaleInheritProp")
		CSerializer.Bool(ifstream,Data,"useParentAlpha")
		CSerializer.Bool(ifstream,Data,"useParentColor")
		if jdVersion != "2014":
			CSerializer.Bool(ifstream,Data,"removeWithParent")
		return Data