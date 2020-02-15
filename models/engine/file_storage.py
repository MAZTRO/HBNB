#!/usr/bin/python3
""" Class FileStorage """


class FileStorage():
	""" FileStorage """
	__file_path = "file.json"
	__objects = {}

	def all(self):
		return (FileStorage.__objects)

	def new(self, obj):
		key = obj.__class__.__name__ + "." + obj.id
		FileStorage.__objects[key] = obj.__dict__
		print("\n**********")
		print(FileStorage.__objects)
		print("**********\n")

	def save(self):
		pass

	def reload(self):
		pass
