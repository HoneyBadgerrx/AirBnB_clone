#!/usr/bin/python3
"""review module for rev class"""

from models.base_model import BaseModel

class Review(BaseModel):
	"""review class to contain review data"""
	place_id = ''
	user_id = ''
	text = ''
