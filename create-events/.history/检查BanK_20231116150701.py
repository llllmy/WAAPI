import WA as wa
get = wa.get_audio_getSelectedObjects()

wa.client.disconnect()

def BankgetInclusions(id):

    getopts ={
        "soundbank":id
    }

    return wa.client.call("ak.wwise.core.soundbank.getInclusions",getopts)
print(get[0]["id"])
print(get)
help(get)
print(BankgetInclusions(get[0]["id"]))