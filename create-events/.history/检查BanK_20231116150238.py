import WA as wa
get = wa.get_audio_getSelectedObjects()

wa.client.disconnect()

def BankgetInclusions(id):

    getopts ={
        "soundbank":id
    }

    return wa.client.call("ak.wwise.core.soundbank.getInclusions", options=getopts)
print(get[0]["id"])
print(get)
print(BankgetInclusions(get[0]["id"]))