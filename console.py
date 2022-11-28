#!/usr/bin/python3
"""
module containing console execution
"""

import cmd
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import re
import shlex

class HBNBCommand(cmd.Cmd):
	"""the console module"""
	intro = 'Welcome to the turtle shell. Type help or ? to list commands\n'
	prompt = '(hbnb) '
	allowed_classes = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']

	def do_quit(self, arg):
		"""exits the console"""
		return True
	def do_EOF(self, arg):
		"""exits the console on eof passed"""
		return True
	def emptyline(self):
		"""what to do when empty line is passed"""
		pass
	def do_create(self, arg):
		"""creates new object from class. Inherits from BaseModel"""
		command = self.parseline(arg)[0]
		if command is None:
			print('** class name missing **')
		elif command not in self.allowed_classes:
			print("** class doesn't exist **")
		else:
			new_obj = eval(command)()
			new_obj.save()
			print(new_obj.id)
	def do_show(self, arg):
		"""prints str repr of instance based on class and id"""
		command = self.parseline(arg)[0]
		iden = self.parseline(line)[1]
		if command is None:
			print("** class name missing **")
		elif command not in self.allowed_classes:
			print("** class doesn't exist **")
		elif iden is None:
			print("** instance id missing **")
		elif storage.all().get(command + '.' + arg) == None:
			print("** no instance found **")
		else:
			print(storage.all().get(command + '.' + arg))

	def do_destroy(self, line):
		"""Deletes an instance based on the class name and id"""
		command = self.parseline(line)[0]
		arg = self.parseline(line)[1]

		if command is None:
			print('** class name missing **')
		elif command not in self.allowed_classes:
			print("** class doesn't exist **")
		elif arg == '':
			print('** instance id missing **')
		else:
			key = command + '.' + arg
			inst_data = models.storage.all().get(key)
			if inst_data is None:
				print('** no instance found **')
			else:
				del models.storage.all()[key]
				models.storage.save()

	def do_all(self, line):
		"""Prints all string representation of all instances"""
		command = self.parseline(line)[0]
		objs = models.storage.all()

		if command is None:
			print([str(objs[obj]) for obj in objs])
		elif command in self.allowed_classes:
			keys = objs.keys()
			print([str(objs[key]) for key in keys if key.startswith(command)])
		else:
			print("** class doesn't exist **")

	def get_objects(self, instance=''):
		"""gets instances of given class or returns all instances"""
		objects = storage.all()

		if instance:
			keys = objects.keys()
			return [str(val) for key, val in objects.items() if key.startswith(instance)]
		return [str(val) for key, val in objects.items()]

	def do_update(self, line):
		"""Updates an instance"""
		args = shlex.split(line)
		args_size = len(args)

		if args_size == 0:
			print('** class name missing **')
		elif args[0] not in self.allowed_classes:
			print("** class doesn't exist **")
		elif args_size == 1:
			print('** instance id missing **')
		else:
			key = args[0] + '.' + args[1]
			inst_data = models.storage.all().get(key)
		if inst_data is None:
			print('** no instance found **')
		elif args_size == 2:
			print('** attribute name missing **')
		elif args_size == 3:
			print('** value missing **')
		else:
			args[3] = self.analyze_parameter_value(args[3])
			setattr(inst_data, args[2], args[3])
			setattr(inst_data, 'updated_at', datetime.now())
			models.storage.save()

	def default(self, line):
		"""if syntax is not recognized, call this function"""
		if '.' in line:
			splitted = re.split(r'\.|\(|\)', line)
			class_name = splitted[0]
			method_name = splitted[1]

		if class_name in self.allowed_classes:
			if method_name == 'all':
				print(self.get_objects(class_name))
			elif method_name == 'count':
				print(len(self.get_objects(class_name)))
			elif method_name == 'show':
				class_id = splitted[2][1:-1]
				self.do_show(class_name + ' ' + class_id)
			elif method_name == 'destroy':
				class_id = splitted[2][1:-1]
				self.do_destroy(class_name + ' ' + class_id)
if __name__ == '__main__':
	HBNBCommand().cmdloop()
