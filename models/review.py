#!/usr/bin/python3
""" This module is a class for Review"""


import models
from models.base_model import BaseModel


class Review(BaseModel):
    """ This is the class Review which inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
