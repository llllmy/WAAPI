import WA as wa

def createRandm(audioname,parent):

    audioname = audioname.replace(" ", "_")
    args = {
        "parent": parent,
        "type": "RandomSequenceContainer",
        "name": audioname  
        #"autoAddToSourceControl": True
    }
    return wa.client.call("ak.wwise.core.object.create", args)
def BankAdd(object,parent):
    #print(bank)
    args = {
            "object": object,
            "parent": parent

        }
    return wa.client.call("ak.wwise.core.object.move", args)


get = wa.get_audio_getSelectedObjects()["objects"]
allname  =[]
for Objects in get:
    for i in wa.get_children(Objects["id"])["return"]:
        print(i)
        
        #print(Objects["name"][:-3])
        if i["name"][:-3] not in allname:
            allname.append(i["name"][:-3])
for i in allname:
    createRandm(i,get[0]["id"])
               
wa.client.disconnect()

