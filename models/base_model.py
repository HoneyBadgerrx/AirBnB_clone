#!/usr/bin/env python3

"""
BaseModel that all other classes will inherit from
"""

import uuid
import datetime
import models

class BaseModel():
	"""attributes all other classes will inherit from"""
	def __init__(self, *args, **kwargs):
		"""initializes with the following variables"""
		if kwargs:
			for arg, value in kwargs.items():
				if arg in ('created_at', 'updated_at'):
					value = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
				if arg != '__class__':
					setattr(self, arg, value)
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.datetime.now()
			self.updated_at = self.created_at
			models.storage.new(self)

	def save(self):
		"""updates updated_at variable with current time"""
		self.updated_at = datetime.datetime.now()
		models.storage.save()

	def to_dict(self):
		"""returns dict containing all keys/values of the object"""
		dic = self.__dict__.copy()
		dic["__class__"] = self.__class__.__name__
		dic["created_at"] = self.created_at.isoformat()
		dic["updated_at"] = self.updated_at.isoformat()

		return dic

	def __str__(self):
		"""string repr of object"""
		return ("[{}] ({}) {}".format(self.__class__.__name__,
 self.id, self.__dict__))
