#!/usr/bin/python3
import json


class FileStorage:
    __file_path = 'db.json'
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return (self.__objects)  # pass by reference ok?

    def new(self, obj):
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            json_dict = {}
            for k, v in self.__objects.items():
                json_dict[k] = v.to_dict()
            json.dump(json_dict, f, indent=2)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                from models.base_model import BaseModel
                from models.user import User
                from models.place import Place
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.review import Review
                classes = {
                    'Amenity': Amenity,
                    'BaseModel': BaseModel,
                    'City': City,
                    'Place': Place,
                    'Review': Review,
                    'State': State,
                    'User': User
                }
                # json data may be malformed, handle that? 👇
                json_dict = json.load(f)
                for k, v in json_dict.items():
                    self.__objects[k] = classes[v['__class__']](**v)
        except FileNotFoundError:
            pass
