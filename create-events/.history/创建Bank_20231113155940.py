import WA as wa

get = wa.get_audio_getSelectedObjects()["objects"]
for Objects in get:
    getD = wa.get_descendants(Objects["id"])['return']
    for i in getD:
        None
        #print(i)


ggg()                   
wa.client.disconnect()

