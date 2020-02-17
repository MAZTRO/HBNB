#!/usr/bin/python3
import json
from models.base_model import BaseModel
import models
""" Class FileStorage """


class FileStorage():
	""" FileStorage """
	__file_path = "file.json"
	__objects = {}

	def all(self):
		return (FileStorage.__objects)

	def new(self, obj):
		key = obj.__class__.__name__ + "." + obj.id
		FileStorage.__objects[key] = obj

	def save(self):
		dict_copy = {}
		for k, val in FileStorage.__objects.items():
			dict_copy[k] = val.to_dict()

		with open(FileStorage.__file_path, 'w') as f:
			f.write(json.dumps(dict_copy))

	def reload(self):
		try:
			with open(FileStorage.__file_path, 'r') as f:
				data = json.loads(f.read())
				for k, v in data.items():
					token = k.split('.')
					obj = BaseModel(**v)
					self.__objects[k] = obj
		except:
			pass
