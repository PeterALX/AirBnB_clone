#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        d = {}
        for k, v in self.__dict__.items():
            if isinstance(v, datetime):
                d[k] = v.isoformat()
            else:
                d[k] = v
        d['__class__'] = self.__class__.__name__
        return (d)
