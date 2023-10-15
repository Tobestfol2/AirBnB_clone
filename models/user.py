#!/usr/bin/python3
"""A user class that inherit from BaseModel"""

from models.base_model import BaseModel
import models


class User(BaseModel):
    """Represent a user class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
