from UAF.Classes.GraphicComponent import Object as GraphicComponent
from UAF.Classes.GFXMaterialSerializable import Object as GFXMaterialSerializable
class Object:
	ENUM_anchor = {
		0: "TEXTURE_ANCHOR_TOP_LEFT",
		1: "TEXTURE_ANCHOR_MIDDLE_CENTER",
		2: "TEXTURE_ANCHOR_MIDDLE_LEFT",
		3: "TEXTURE_ANCHOR_MIDDLE_RIGHT",
		4: "TEXTURE_ANCHOR_TOP_CENTER",
		5: "TEXTURE_ANCHOR_TOP_RIGHT",
		6: "TEXTURE_ANCHOR_BOTTOM_CENTER",
		7: "TEXTURE_ANCHOR_BOTTOM_LEFT",
		8: "TEXTURE_ANCHOR_BOTTOM_RIGHT",
		9: "TEXTURE_ANCHOR_CUSTOM"
	}
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False,flags=None):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		
		Data.update(GraphicComponent.Serialize(CSerializer,ifstream,jdVersion,sizeOf))
		if jdVersion != "2014":
			CSerializer.uint32(ifstream,Data,"AtlasIndex")
		CSerializer.ENUM(ifstream,Data,"anchor")
		CSerializer.Vector2(ifstream,Data,"customAnchor")
		Data['material'] = GFXMaterialSerializable.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		CSerializer.Vector3(ifstream,Data,"SinusAmplitude")
		CSerializer.float32(ifstream,Data,"SinusSpeed")
		CSerializer.Angle(ifstream,Data,"AngleX")
		CSerializer.Angle(ifstream,Data,"AngleY")
		CSerializer.ENUM(ifstream,Data,"oldAnchor")
		
		
		Data['__class'] = "MaterialGraphicComponent"
		

		return Data