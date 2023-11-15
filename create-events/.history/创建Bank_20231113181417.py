import WA as wa

get = wa.get_audio_getSelectedObjects()["objects"]

while True:
    Eve = True
    for Objects in get:
    #print(Objects["path"][:6])
        if Objects["path"][:6] != "\Event":
            Eve=False;
    if Eve:
        input("Press Enter to continue...")
        continue
    else:
        break
   
# for Objects in get:
#     print(Objects["path"][:6])
    #if Objects["path"][:6] != "\Event":

    # getD = wa.get_descendants(Objects["id"])['return']
    # for i in getD:
    #     None
        #print(i)


               
wa.client.disconnect()

