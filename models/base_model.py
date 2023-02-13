#!/usr/bin/python3
""" class BaseModel defined here """
import uuid
from datetime import datetime 
# from models import storage
import models

class BaseModel:
    """ class BaseModel is the base class for all other models, defining common functionalities save, __str__, save and to_dict"""
    def __init__(self, *args, **kwargs):
        """ initialization of instance """
        if (kwargs):
            if("id" not in kwargs or "created_at" not in kwargs or "updated_at" not in kwargs):
                #raise them errors.
                print("raise an error here: either created_at or updated_at doesn't exist ")
                return
            for (key, value) in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at # potential bug, as the assignment seems to require separate new date here
            models.storage.new(self)

    def __str__(self):
        """ returns a string represantation of class """
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """ updates a BaseModel instance's updated_at property and saves changes to disk when called"""
        self.updated_at = datetime.now() 
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary represantion of the class. This dictionary is used for serialization into json for storage in disk """
        my_dict = self.__dict__.copy() #potential bugs here, consider doing a deepcopy instead
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
