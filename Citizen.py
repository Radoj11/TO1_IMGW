class Citizen:
    def __init__(self, id, name, last_name):
        self.__id = id
        self.__name = name
        self.__last_name = last_name

    def get_name():
        return self.__name

    def get_last_name():
        return self.__last_name

    def get_id():
        return self.__id

    def get_full_name():
        return self.__name + " " + self.__last_name
