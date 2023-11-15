import WA as wa
import cProfile

def your_code():
    get = wa.get_audio_getSelectedObjects()["objects"]
    for Objects in get:
        getD = wa.get_descendants(Objects["id"])['return']
        for i in getD:
            print(i)
    wa.client.disconnect()
cProfile.run('your_code()')
