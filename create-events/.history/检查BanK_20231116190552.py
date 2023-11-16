import WA as wa
from waapi import WaapiClient
get = wa.get_audio_getSelectedObjects()
client = WaapiClient()
#wa.client.disconnect()

def BankgetInclusions(id):

    getopts ={
        "soundbank":id
    }

    return wa.client.call("ak.wwise.core.soundbank.getInclusions",getopts)

#print(get[0]["id"])
#print(get)
#help(get)
print(BankgetInclusions(get[0]["id"]))
client.disconnect()