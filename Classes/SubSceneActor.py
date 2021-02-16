from UAF.Classes.Actor import Object as Actor
from UAF.Classes.Scene import Object as Scene
class Object:
	ENUM_viewType = {
		0: "VIEWTYPE_MAIN",
		1: "VIEWTYPE_REMOTE",
		2: "VIEWTYPE_ALL",
		3: "VIEWTYPE_NONE"
	}
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False,flags=None):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data.update(Actor.Serialize(CSerializer,ifstream,jdVersion,sizeOf,flags))
		Data['__class'] = "SubSceneActor"
		CSerializer.Path(ifstream,Data,"RELATIVEPATH")
		CSerializer.uint32(ifstream,Data,"EMBED_SCENE")
		CSerializer.uint32(ifstream,Data,"IS_SINGLE_PIECE")
		CSerializer.uint32(ifstream,Data,"ZFORCED")
		CSerializer.uint32(ifstream,Data,"DIRECT_PICKING")
		CSerializer.uint32(ifstream,Data,"IGNORE_SAVE")
		CSerializer.ENUM(ifstream,Data,"viewType")
		Data['SCENE'] = Scene.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		
		
		return Data