from StateDeviceManager import StateDeviceManager
from states import States

class Notifier:
    def __init__(self):
        self.__deviceStateList = {x.value:x for x in list(States)}

    def send_message(notification, state):
        print("xd")

