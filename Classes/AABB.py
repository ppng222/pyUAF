class Object:
    @staticmethod
    def Serialize(CSerializer,ifstream,jdVersion,sizeOf=False,flags=None):
        Data = {}
        Data['__class'] = "AABB"
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
        CSerializer.Vector2(ifstream,Data,"MIN")
        CSerializer.Vector2(ifstream,Data,"MAX")
        return Data