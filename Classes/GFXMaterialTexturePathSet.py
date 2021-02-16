class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False,flags=None):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()	
		
		Data['__class'] = "GFXMaterialTexturePathSet"
		
		CSerializer.Path(ifstream,Data,"diffuse")
		CSerializer.Path(ifstream,Data,"back_light")
		CSerializer.Path(ifstream,Data,"normal")
		CSerializer.Path(ifstream,Data,"separateAlpha")
		CSerializer.Path(ifstream,Data,"diffuse_2")
		CSerializer.Path(ifstream,Data,"back_light_2")
		CSerializer.Path(ifstream,Data,"anim_impostor")
		CSerializer.Path(ifstream,Data,"diffuse_3")
		CSerializer.Path(ifstream,Data,"diffuse_4")
		
		
		return Data