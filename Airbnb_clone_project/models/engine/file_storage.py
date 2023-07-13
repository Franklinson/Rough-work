#!/usr/bin/python3

class FileStorage:
    def __init__(self):

     __file_path = "file.json"

     __objects = {}



    def all(self):
        return self.__objects

    def new(self, ojb):
        k = "{}.{}".format(type(obj).__name__, obj.id)
        self.__object[k] = obj

    def save(self):
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj = eval(class_name).from_dict(value)
                    self.__objects[key] = obj


