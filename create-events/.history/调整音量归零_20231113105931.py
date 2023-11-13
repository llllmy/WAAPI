import WA as wa




get = wa.get_audio_getSelectedObjects()["objects"]
for Objects in get:
    getD = wa.get_descendants(Objects["id"])['return']
    for i in getD:
        #print(
        wa.setVolume(i["id"], 0)

wa.client.disconnect()