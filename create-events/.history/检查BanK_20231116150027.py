import WA as wa
get = wa.get_audio_getSelectedObjects()

wa.client.disconnect()

def BankgetInclusions(id):

    getResult = {
        "soundbank":id
    }

    return wa.client.call("ak.wwise.core.soundbank.getInclusions", getResult)
print(get[0]["id"])
print(BankgetInclusions(get[0]["id"]))