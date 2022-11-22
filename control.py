#!/usr/bin/python3
import cmd
class test(cmd.Cmd):
	intro = 'Welcome to the turtle shell. Type help or ? to list commands\n'
	prompt = '(turtle) '
	file = None
test().cmdloop()
