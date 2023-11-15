import WA as wa



while True:
    get = wa.get_audio_getSelectedObjects()["objects"]
    Eve = False
    input('这条信息后选择事件(Events)位置后按Enter:')
    for Objects in get:
    #print(Objects["path"][:6])
        if Objects["path"][:6] != "\Event":
            Eve=True;
    if Eve:
        #input("Press Enter to continue...")
        continue
    else:
        break
   
for Objects in get:
    print(Objects["path"][:6])
    if Objects["path"][:6] != "\Event":

    # getD = wa.get_descendants(Objects["id"])['return']
    # for i in getD:
    #     None
    #     print(i)


               
wa.client.disconnect()

