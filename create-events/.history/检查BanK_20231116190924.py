import WA as wa
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

get = get_audio_getSelectedObjects()
print(get)
getopts ={
        "soundbank":get[0]["id"]
    }

bi = client.call("ak.wwise.core.soundbank.getInclusions",getopts)

#print(get[0]["id"])
#print(get)
#help(get)
print(bi)
client.disconnect()