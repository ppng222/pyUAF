from UAF.Classes.PlaybackEvent import Object as PlaybackEvent
from UAF.Classes.AutoDanceFxDesc import Object as AutoDanceFxDesc
from UAF.Classes.FxEvent import Object as FxEvent
from UAF.Classes.PropEvent import Object as PropEvent
from UAF.Classes.AutodancePropData import Object as AutodancePropData
from UAF.Classes.PropPlayerConfig import Object as PropPlayerConfig
class Object:
	@staticmethod
	def Serialize(CSerializer,ifstream,jdVersion,sizeOf=True):
		Data = {}
		CSerializer.sizeOf(ifstream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "JD_AutodanceVideoStructure"
		CSerializer.uint32(ifstream,Data,"GameMode")
		CSerializer.float32(ifstream,Data,"SongStartPosition") 
		CSerializer.float32(ifstream,Data,"Duration") 
		CSerializer.float32(ifstream,Data,"ThumbnailTime") 
		CSerializer.float32(ifstream,Data,"FadeOutDuration") 
		CSerializer.Path(ifstream,Data,"AnimatedFramePath",jdVersion=jdVersion)
		CSerializer.Path(ifstream,Data,"GroundPlanePath",jdVersion=jdVersion)
		CSerializer.Path(ifstream,Data,"FirstLayerTripleBackgroundPath",jdVersion=jdVersion)
		CSerializer.Path(ifstream,Data,"SecondLayerTripleBackgroundPath",jdVersion=jdVersion)
		CSerializer.Path(ifstream,Data,"ThirdLayerTripleBackgroundPath",jdVersion=jdVersion)
		CSerializer.CList("PlaybackEvent",ifstream,Data,"playback_events",jdVersion)
		Data['background_effect'] = AutoDanceFxDesc.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		CSerializer.CList("FxEvent",ifstream,Data,"background_effect_events",jdVersion)
		Data['player_effect'] = AutoDanceFxDesc.Serialize(CSerializer,ifstream,jdVersion,sizeOf)
		CSerializer.CList("FxEvent",ifstream,Data,"player_effect_events",jdVersion)
		CSerializer.CList("PropEvent",ifstream,Data,"prop_events",jdVersion)
		CSerializer.CList("AutodancePropData",ifstream,Data,"props",jdVersion)
		CSerializer.CList("PropPlayerConfig",ifstream,Data,"props_players_config",jdVersion)
		
		return Data