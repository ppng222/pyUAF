from UAF.Classes.AABB import Object as AABB
from UAF.Classes.PolyPointList import Object as PolyPointList
class Object:
    class Connection:
        @staticmethod
        def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False):
            Data = {}
            CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
            Data['__class'] = "Connection"
            CSerializer.uint32(ifstream,Data,"PreviousId")
            CSerializer.Vector2(ifstream,Data,"PosInit")
            return Data
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False,flags=None):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "PolyLine"
        Data['PolyPointList'] = PolyPointList.Serialize(CSerializer,ifstream,jdVersion,sizeOf=False)
        Data['AABB'] = AABB.Serialize(CSerializer,ifstream,jdVersion,sizeOf=False)
        Data['Connection'] = Object.Connection.Object.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		return Data