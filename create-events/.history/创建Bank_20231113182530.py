import WA as wa

def createBank(audioname,auidoid,parent):
    # newEvent="Play_"+audioname
    # if oldEvent == newEvent:
    #     print(newEvent+"已存在")
    #     return
    audioname = audioname.replace(" ", "")
    args = {
        "parent": parent,
        "type": "SoundBank",
        "name": audioname,  
        "autoAddToSourceControl": True, 
        "children": [
        {
            # "type": "Action",
            # "name": "",
            # "@ActionType": 1,
            "@Target": auidoid
            # "@FadeTime": FadeTime,
            # "@Delay": Delay
        }
        ]
    }
    return wa.client.call("ak.wwise.core.object.create", args)


# while True:
#     get = wa.get_audio_getSelectedObjects()["objects"]
#     Eve = False
#     input('这条信息后选择事件(Events)位置后按Enter:')
#     for Objects in get:
#     #print(Objects["path"][:6])
#         if Objects["path"][:6] != "\Event":
#             Eve=True;
#     if Eve:
#         #input("Press Enter to continue...")
#         continue
#     else:
#         break
get = wa.get_audio_getSelectedObjects()["objects"]
for Objects in get:
    print(Objects["path"])
    if Objects["path"][:6] != "\Event":
        createBank(Objects["name"],Objects["id"],r"\SoundBanks\Default Work Unit")
    # getD = wa.get_descendants(Objects["id"])['return']
    # for i in getD:
    #     None
    #     print(i)


               
wa.client.disconnect()

