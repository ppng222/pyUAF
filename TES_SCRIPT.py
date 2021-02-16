import importlib
import CSerializerObjectBinary_sizeOf as CSerializerObject 
ifstream = open(r"F:\JDHitsWii_OLD\Files\FST\BundleLogic\cache\itf_cooked\wii\world\ui\screens\title\animations\enter_forward.tape.ckd",'rb')
ifstream.seek(0x49B)
CSerializer = getattr(importlib.import_module("Classes.SizeClip"),"Object")
CSerializer.Serialize(CSerializerObject,ifstream,"new")