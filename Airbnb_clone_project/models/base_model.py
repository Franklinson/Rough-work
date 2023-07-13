#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    def __init__(self, *args, **kwargs):

        time= "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for k, v in kwargs.items():
                if k == "created" or k == "update" and k != "__class__":
                    self.__dict__[k] = datetime.strptime(v, time)
                else:
                    self.__dict__[k] = v

        else:
            self.id = str(uuid.uuid4())
            self.update = datetime.today()
            self.created = datetime.today()
            storage.new(self)
        


    def __str__(self):
        return "[{}, ({}), {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.update = datetime.today()
        storage.save()

    def my_dict(self):
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created"] = self.created.isoformat()
        my_dict["update"] = self.update.isoformat()

        return my_dict
