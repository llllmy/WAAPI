import WA as wa

get = wa.get_audio_getSelectedObjects()["objects"]
for Objects in get:
    print(Objects)
    #if Objects["type"] == "audio":
    # getD = wa.get_descendants(Objects["id"])['return']
    # for i in getD:
    #     None
        #print(i)


               
wa.client.disconnect()

