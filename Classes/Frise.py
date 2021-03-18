from UAF.Classes.Pickable import Object as Pickable
from UAF.Classes.PolyPointList import Object as PolyPointList
class Object:
	class CollisionData:
		class Object:
			@staticmethod
			def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
				Data = {}
            	CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
				CSerializer.CList("PolyPointList",ifstream,Data,"LocalCollisionList",jdVersion)
				CSerializer.CList("PolyLine",ifstream,Data,"WorldCollisionList",jdVersion)
				return Data
	class MeshStaticData:
		class Object:
			@staticmethod
			def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
				pass
	class MeshAnimData:
		class Object:
			@staticmethod
			def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
				pass
	class MeshOverlayData:
		class Object:
			@staticmethod
			def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
				pass
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False,flags=None):
		Data = {}
		Data['__class'] = "Frise"
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data.update(Pickable.Serialize(CSerializer,ifstream,jdVersion,sizeOf,flags))
		
		print("Frise")
		CSerializer.Color(ifstream,Data,"EventShowColorDst")
		
		return Data