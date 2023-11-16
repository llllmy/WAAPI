import WA as wa
get = wa.get_audio_getSelectedObjects()

wa.client.disconnect()

def BankgetInclusions(id):

    getopts = {
        "soundbank":id
    }

    getResult = {
        
    }

    return wa.client.call("ak.wwise.core.soundbank.getInclusions", getResult, options=getopts)

print(BankgetInclusions(get[0]["id"]))