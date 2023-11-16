import WA as wa
get = wa.get_audio_getSelectedObjects()
print(get)
wa.client.disconnect()

def BankgetInclusions ():

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
ak.wwise.core.soundbank.getInclusions