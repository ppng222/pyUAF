class Object:
	ENUM_gfxOccludeInfo = {
		0: "GFX_OCCLUDE_INFO_DEFAULT",
		1: "GFX_OCCLUDE_INFO_BIG_OPAQUE",
		2: "GFX_OCCLUDE_INFO_SMALL_OR_TRANSPARENT"
	}
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False,flags=None):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "GFXPrimitiveParam"
		CSerializer.Color(ifstream,Data,"colorFactor")
		if jdVersion == "2014":
			CSerializer.float32(ifstream,Data,"FrontLightBrightness")
			CSerializer.float32(ifstream,Data,"FrontLightContrast")
			CSerializer.float32(ifstream,Data,"BackLightBrightness")
			CSerializer.float32(ifstream,Data,"BackLightContrast")
			CSerializer.Color(ifstream,Data,"colorFog")
			CSerializer.float32(ifstream,Data,"DynamicFogFactor")
			CSerializer.uint32(ifstream,Data,"RenderInReflections")
		CSerializer.ENUM(ifstream,Data,"gfxOccludeInfo")


		return Data