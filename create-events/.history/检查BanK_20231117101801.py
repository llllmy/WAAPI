#import WA as wa
from waapi import WaapiClient

client = WaapiClient()
#wa.client.disconnect()

def get_audio_getSelectedObjects():

    getopts = {
        "return": [
            "name",
            "path",
            "id",
            "type"
        ]
    }

    getResult = {
    }

    return client.call("ak.wwise.ui.getSelectedObjects", getResult, options=getopts)['objects']
    
def get_descendants(sound_sfx_guid):

    args = {
        "from": {
            "id": [
                sound_sfx_guid
            ]
        },
        "transform": [
            {"select": ['descendants']}
        ]
    }


    opts = {
        "return": [
            "name","id","type","path"
        ]
    }

    return client.call("ak.wwise.core.object.get", args, options=opts)
def getInclusions(id):

    getopts ={
        "soundbank":id
    }

    getResult = {
    }

    return client.call("ak.wwise.core.soundbank.getInclusions",getopts)
    


get = get_audio_getSelectedObjects()
#print(get)
for g in get:
    #print(g)
    for i in get_descendants(g["id"])["return"]:

        #print(i["type"])
        if i["type"] == "SoundBank":
        #print(getInclusions(i["id"])["inclusions"])
            for z in getInclusions(i["id"])["inclusions"]:
                #print(z["filter"])['events', 'structures', 'media']
                if ("media" not in z["filter"])|("media" not in z["events"])|("structures" not in z["filter"]):
                    #print(z["filter"])
                    print(i["name"])
    


#bi = client.call("ak.wwise.core.soundbank.getInclusions",getopts)

#print(get[0]["id"])["filter"]
#print(get)
#help(get)

client.disconnect()