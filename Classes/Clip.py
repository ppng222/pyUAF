class sizeOf:
	@staticmethod
	def getSizeOf(Data):
		return 0x18
class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {"__class":"Clip"}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		CSerializer.uint32(ifstream,Data,'Id',)
		CSerializer.uint32(ifstream,Data,'TrackId')
		CSerializer.uint32(ifstream,Data,'IsActive')
		CSerializer.int32(ifstream,Data,'StartTime')
		CSerializer.int32(ifstream,Data,'Duration')
		return Data