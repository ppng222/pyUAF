class Object:
	@staticmethod
	def Serialize(CSerializer,ifStream,jdVersion,sizeOf=True):
		# List of all possible clips
		TapeClip = ['ActorEnableClip', 'AlphaClip', 'AnimationClip', 'ColorClip', 'FXClip', 'GameplayEventClip', 'MarkerClip', 'MaterialGraphicAlphaThresholdClip', 'MaterialGraphicDiffuseAlphaClip', 'MaterialGraphicDiffuseColorClip', 'MaterialGraphicEnableLayerClip', 'MaterialGraphicUVAnimRotationClip', 'MaterialGraphicUVRotationClip', 'MaterialGraphicUVScaleClip', 'MaterialGraphicUVScrollClip', 'MaterialGraphicUVTranslationClip', 'PivotClip', 'RotationClip', 'ScaleClip', 'ProportionClip', 'SizeClip', 'SoundwichClip', 'SoundSetClip', 'SpawnActorClip', 'TapeLauncherClip', 'TapeReferenceClip', 'TextClip', 'TranslationClip','CameraFeedClip','CommunityDancerClip','GoldEffectClip','HideUserInterfaceClip','KaraokeClip','MashupClip','SlotClip','VideoClip','MotionClip','PictogramClip','UICollBoxClip']
		TapeTrack = ['CommunityDancerTrack','GoldEffectTrack','KaraokeTrack','MoveTrack','PictoTrack']
		MetaInfo = ['KaraokeMetaInfo']
		# tape Constructor
		Data = {}
		CSerializer.uint32(ifStream,raw=True) ## always 1
		CSerializer.sizeOf(ifStream,Data) if sizeOf else CSerializer.NULL()
		CSerializer.uint32(ifStream,raw=True) ## __class
		CSerializer.sizeOf(ifStream,Data) if sizeOf else CSerializer.NULL()
		Data['__class'] = "Tape"
		CSerializer.CList_Factory(TapeClip,ifStream,Data,"Clips",jdVersion)
		CSerializer.CList_Factory(TapeTrack,ifStream,Data,"Tracks",jdVersion)
		CSerializer.CList_Factory(MetaInfo,ifStream,Data,"MetaInfos",jdVersion)
		if jdVersion == "new":
			CSerializer.CList("ObjectPath",ifStream,Data,"ActorPaths",jdVersion)
		
		CSerializer.uint32(ifStream,Data,"TapeClock")
		if jdVersion != "2014":
			CSerializer.uint32(ifStream,Data,"TapeBarCount")
			CSerializer.uint32(ifStream,Data,"FreeResourcesAfterPlay")
			CSerializer.String8(ifStream,Data,"MapName")
		
		return Data