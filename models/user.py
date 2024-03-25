#!/usr/bin/python3
"""This is class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """This is the user model, repping a user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
