import WA as wa
from waapi import WaapiClient
get = wa.get_audio_getSelectedObjects()
client = WaapiClient()
#wa.client.disconnect()


getopts ={
        "soundbank":get[0]["id"]
    }

bi = client.call("ak.wwise.core.soundbank.getInclusions",getopts)

#print(get[0]["id"])
#print(get)
#help(get)
print(bi)
client.disconnect()