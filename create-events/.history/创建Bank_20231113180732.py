import WA as wa

get = wa.get_audio_getSelectedObjects()["objects"]

while True:
    for Objects in get:
    #print(Objects["path"][:6])
        if Objects["path"][:6] != "\Event":
            input("Press Enter to continue...")
            continue
    break
for Objects in get:
    print(Objects["path"][:6])
    if Objects["path"][:6] != "\Event":

    # getD = wa.get_descendants(Objects["id"])['return']
    # for i in getD:
    #     None
        #print(i)


               
wa.client.disconnect()

