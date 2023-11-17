import WA as wa
#from waapi import WaapiClient

#client = WaapiClient()
#wa.client.disconnect()

# def get_audio_getSelectedObjects():

#     getopts = {
#         "return": [
#             "name",
#             "path",
#             "id",
#             "type"
#         ]
#     }

#     getResult = {
#     }

#     return client.call("ak.wwise.ui.getSelectedObjects", getResult, options=getopts)['objects']
    
# def get_descendants(sound_sfx_guid):

#     args = {
#         "from": {
#             "id": [
#                 sound_sfx_guid
#             ]
#         },
#         "transform": [
#             {"select": ['descendants']}
#         ]
#     }


#     opts = {
#         "return": [
#             "name","id","type","path"
#         ]
#     }

#     return client.call("ak.wwise.core.object.get", args, options=opts)

def getInclusions(id):

    getopts ={
        "soundbank":id
    }

    getResult = {
    }

    return wa.client.call("ak.wwise.core.soundbank.getInclusions",getopts)
    
noincl =[]
get = wa.get_audio_getSelectedObjects()
#print(get)
for g in get:
    #print(g)
    for i in wa.get_descendants(g["id"])["return"]:
        #print(i)
        #print(wa.getchildrenCount(i["id"]))
        
        
        #print(i["type"])
        if i["type"] == "SoundBank":
                #print(i)
            if len(wa.getInclusions(i["id"])["inclusions"]) > 0:
               # print(len(wa.getInclusions(i["id"])["inclusions"]))
                #print(getInclusions(i["id"])["inclusions"])
                for z in wa.getInclusions(i["id"])["inclusions"]:

                    #print(z["filter"])#['events', 'structures', 'media']
                    if ("media" not in z["filter"])|("events" not in z["filter"])|("structures" not in z["filter"]):
                        #print(z["filter"])
                        #print(i["name"])
                        noincl.append(i["name"])
print(noincl)

#bi = client.call("ak.wwise.core.soundbank.getInclusions",getopts)

#print(get[0]["id"])["filter"]
#print(get)
#help(get)

wa.client.disconnect()