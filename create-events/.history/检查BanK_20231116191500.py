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
print(get)

for i in get_descendants(get[0]["id"]):
    print(i)
    getInclusions(i["id"])


#bi = client.call("ak.wwise.core.soundbank.getInclusions",getopts)

#print(get[0]["id"])
#print(get)
#help(get)
print(bi)
client.disconnect()