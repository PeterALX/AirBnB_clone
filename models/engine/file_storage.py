#!/usr/bin/python3
""" class Filestorage """
import json
from models.base_model import BaseModel

class FileStorage:
    """ 
    This class handles storage:
            serialisation of models to json to store into disk,
            reloading data from disk on app startup
            keeping disk storage up to date with the apps state
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """no initialization to be done """
        pass
    def all(self):
        """returns __objects"""
        return self.__objects
    def new(self,obj):
        """ adds a model to storage. ie __objects """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
    def save(self):
        """saves __objects to disk """
        dict_objects = dict(self.__objects)
        for key in dict_objects.keys():
            dict_objects[key] = dict_objects[key].to_dict()
        jayson= json.dumps(dict_objects, indent=8) # probably remove this indent for checker
        with open(self.__file_path, "w") as file:
            file.write(jayson)


    # def reload(self):
    #     """ reloads data from disk when app is initialized """
    #     class_list = {
    #             "BaseModel":BaseModel
    #     }
    #     json_string = ""
    #     try:
    #         with open(self.__file_path, "r", encoding="utf-8") as file:
    #             json_string = file.read() #read the json into an empty string first because apparently json.dumping an empty file throws an error
    #     except FileNotFoundError:
    #         pass
    #     if len(json_string) == 0:
    #         return
    #     dict_objects = json.loads(json_string)
    #     for (key, value) in dict_objects.items():
    #         self.__objects[key] = class_list[value["__class__"]](**value)

    def reload(self):
        """Deserializes the JSON file to __objects only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as myFile:
                my_obj_dump = myFile.read()
        except Exception:
            return
        objects = eval(my_obj_dump)
        for (key, value) in objects.items():
            objects[key] = eval(key.split('.')[0] + '(**value)')
        self.__objects = objects

    def delete(self, obj):
        """Deletes obj from __objects
            """
        try:
            key = obj.__class__.__name__ + "." + str(obj.id)
            if key in self.__objects.keys():
                del self.__objects[key]
            self.save()
            return True
        except Exception:
            return False
