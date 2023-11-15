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
def Move(object,parent):
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
allRandm =[]
for i in allname:
    randm = createRandm(i,get[0]["id"])
    allRandm.append(randm)
for Objects in get:
    for i in wa.get_children(Objects["id"])["return"]:
        print(i["name"])
        if i["name"][:-3] in allname:
            Move(i["id"],allRandm[allname.index(i["name"][:-3])]["id"])

wa.client.disconnect()

