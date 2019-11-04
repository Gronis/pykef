def test_main_1():
    host = "192.168.178.52"
    port = 50001
    speaker = KefSpeaker(host, port)
    # print(speaker.__setSource(InputSource.Opt))
    # print(speaker.__getSource())

    # TIMER = 0.1
    # sleep(TIMER)
    # speaker.connect(host, port)
    # sleep(TIMER)
    # print(speaker.volume)
    # sleep(TIMER)
    # print(speaker.volume)
    # sleep(TIMER)
    # print(speaker.volume)
    # sleep(TIMER)
    # sleep(TIMER)
    # print(speaker.volume)
    # sleep(TIMER)
    speaker.source = InputSource.Usb
    print("isOnline:" + str(speaker.online))
    print(speaker.source)
    speaker.volume = 0.5
    print(speaker.volume)
    # print ("vol:" + str(speaker.increaseVolume()))
    speaker.volume = None
    # print("getvol: ", speaker.__getVolume())
    speaker.muted = False
    print("getvol: ", speaker.volume)
    speaker.volume = 0.6
    print("getvol: ", speaker.volume)
    print("vol: ", speaker.volume)
    print("getvol: ", speaker.volume)
    print("vol up:" + str(speaker.increaseVolume(0.05)))
    print("getvol: ", speaker.volume)
    print("vol: ", speaker.volume)
    speaker.increaseVolume()
    print("vol up:" + str(speaker.volume))
    speaker.increaseVolume()
    print("vol up:" + str(speaker.volume))
    speaker.volume = None
    speaker.increaseVolume()
    print("vol up:" + str(speaker.volume))
    speaker.muted = False
    print("vol: ", speaker.volume)
    speaker.decreaseVolume()
    print("vol down:" + str(speaker.volume))
    speaker.decreaseVolume()
    print("vol down:" + str(speaker.volume))
    speaker.decreaseVolume()
    print("vol down:" + str(speaker.volume))

    while 1:
        sleep(3)
        print(speaker.source)


def test_main_2():
    host = "192.168.178.52"
    port = 50001
    service = KefSpeaker(host, port)
    print("isOnline:" + str(service.online))
    service.source = InputSource.Usb
    service.source = InputSource(("USB",))
    # service.turnOff()


def test_main_3():
    host = "192.168.178.52"
    port = 50001
    speaker = KefSpeaker(host, port)

    while 1:
        sleep(2)
        print("vol:" + str(speaker.volume))
        print("mute:" + str(speaker.muted))
        print("source:" + str(speaker.source))
        print("online:" + str(speaker.online))


def test_main_4():
    host = "192.168.178.52"
    port = 50001
    speaker = KefSpeaker(host, port)

    while 1:

        speaker.muted = True
        print("Is Mutted:" + str(speaker.muted))
        sleep(5)
        speaker.muted = False
        print("Is Mutted:" + str(speaker.muted))
        sleep(5)


def test_main_5():
    host = "192.168.178.52"
    port = 50001
    speaker = KefSpeaker(host, port)

    while 1:
        # speaker.increaseVolume(0.1)
        print("Volume:" + str(speaker.volume))
        sleep(5)
        # speaker.decreaseVolume(0.1)
        print("Volume:" + str(speaker.volume))
        sleep(5)

        # speaker.muted = True
        print("Is Mutted:" + str(speaker.muted))
        # sleep(5)
        # speaker.muted = False
        # print("Is Mutted:" + str(speaker.muted))
        # sleep(5)

        sleep(5)
