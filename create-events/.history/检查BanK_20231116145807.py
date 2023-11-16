import WA as wa
get = wa.get_audio_getSelectedObjects()

wa.client.disconnect()

def BankgetInclusions(id):

    getopts = {
            "inclusions": [
        {
            "object": id,
            "filter": [
                "events"

            ]
        }
        ]
    }

    getResult = {
        "soundbank":id
    }

    return wa.client.call("ak.wwise.core.soundbank.getInclusions", getResult, options=getopts)
print(get[0]["id"]))
print(BankgetInclusions(get[0]["id"]))