#!/usr/bin/python3
import uuid
import datetime
""" Class basemodel """


class BaseModel():
    """BaseModel"""

    def __init__(self, id=None, name=None, my_number=None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.my_number = my_number
        self.created_at = str(datetime.datetime.now().isoformat('T'))
        self.update_at = str(datetime.datetime.now().isoformat('T'))

    def save(self):
        self.update_at = str(datetime.datetime.now().isoformat('T'))

    def to_dict(self):
        dic = self.__dict__
        dic['__class__'] = self.__class__.__name__
        return dic

    def __str__(self):
        return ('[{}] ({}) {}'.format(self.__class__.__name__, /
                self.id, self.__dict__))
