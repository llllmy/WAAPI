from waapi import WaapiClient
import re
import WA as wa
#client = waapi.WaapiClient(url="ws://127.0.0.1:8080/waapi")
def recurse_wwise_objects(object_id):
    #print(print(i["id"]))
    #if i["type"]!="Sound":
    gc=wa.get_children(object_id)["return"]
    wa.get_parent(object_id)
    if len(gc)!=0:
            for i in gc:
                #print(i["id"])
                if i["type"]!="Sound":
                    print(i["id"])
                    recurse_wwise_objects(i["id"])
def Iscontainer(object_id):
    if wa.get_audiotype(object_id) =="RandomSequenceContainer"|wa.get_audiotype(object_id)=="SwitchContainer"|wa.get_audiotype(object_id)=="BlendContainer":
        return True
    else:
        return False 
get = wa.get_audio_getSelectedObjects()["objects"][0]
gc=wa.get_children(get["id"])["return"]
if get["type"]!="Sound":
        print(get["type"])
        #recurse_wwise_objects(get["id"])
#print(len(gc))
#recurse_wwise_objects(get["objects"][0]["id"])
wa.client.disconnect()
#WorkUnit Folder ActorMixer