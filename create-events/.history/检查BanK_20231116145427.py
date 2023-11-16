import WA as wa
get = wa.get_audio_getSelectedObjects()
print(get)
wa.client.disconnect()

def BankgetInclusions(id):

    getopts = {

    }

    getResult = {
        "soundbank":id
    }

    return wa.client.call("ak.wwise.core.soundbank.getInclusions", getResult, options=getopts)

