import WA as wa

def createBank(audioname,auidoid,parent,type1):

    audioname = audioname.replace(" ", "_")
    args = {
        "parent": parent,
        "type": "RandomSequenceContainer",
        "name": audioname  
        #"autoAddToSourceControl": True
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
    for i in wa.get_children(Objects["id"])["return"]:
        print(i)
        
        #print(Objects["name"][:-3])
        if i["name"][:-3] not in allname:
            allname.append(i["name"][:-3])


               
wa.client.disconnect()

