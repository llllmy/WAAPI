import WA as wa
get = wa.get_audio_getSelectedObjects()
print(get)
wa.client.disconnect()

def BankgetInclusions ():

    getopts = {

    }

    getResult = {
    }

    return wa.client.call("ak.wwise.core.soundbank.getInclusions", getResult, options=getopts)['objects']

