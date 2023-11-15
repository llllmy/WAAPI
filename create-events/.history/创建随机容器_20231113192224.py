import WA as wa

def createBank(audioname,auidoid,parent,type1):

    audioname = audioname.replace(" ", "_")
    args = {
        "parent": parent,
        "type": "SoundBank",
        "name": audioname,  
        "autoAddToSourceControl": True
    }
    return wa.client.call("ak.wwise.core.object.create", args)
def BankAdd(object,bankid):
    #print(bank)
    args_bank_add = {
            "soundbank": bankid,
            "operation": "add",
            "inclusions": [
                {
                    "object": object,
                    "filter": [
                        "events"
                    ]
                }
            ]
        }
    return wa.client.call("ak.wwise.core.soundbank.setInclusions", args_bank_add)


get = wa.get_audio_getSelectedObjects()["objects"]
allname  =[]
for Objects in get:

        
        print(Objects["name"])
        


               
wa.client.disconnect()

