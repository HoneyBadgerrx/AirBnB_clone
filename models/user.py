#!/usr/bin/python3
"""
user module that inherits from base class
"""

from models.base_model import BaseModel

class User(BaseModel):
	""" the user class"""
	email = ''
	password = ''
	first_name = ''
	last_name = ''
