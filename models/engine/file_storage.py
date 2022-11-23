#!/usr/bin/env python3
"""
module for storing objects created in a json file
"""

import json
from models.base_model import BaseModel
from os import path

class FileStorage:
	"""file storage class"""
	__file_path = "store.json"
	__objects = {}

	def all(self):
		"""returns dictionary of objects"""
		return self.__objects

	def new(self, obj):
		"""places instance in objects"""
		key = obj.__class__.__name__ + '.' + obj.id
		self.__objects[key] = obj

	def save(self):
		"""serialises object dictionary to json file in __file_path"""
		j_dict = {}
		for k, v in self.__objects.items():
			j_dict[k] = v.to_dict()
		with open(self.__file_path, mode='w', encoding='utf-8') as f:
			json.dump(j_dict, f)
	def reload(self):
		"""loads stored objects"""
		if path.exists(self.__file_path):
			with open(self.__file_path, mode='r', encoding='utf-8') as f:
				j_dict = json.load(f)
			for k, v in j_dict.items():
				self.__objects[k] = eval(v['__class__'])(**v)
