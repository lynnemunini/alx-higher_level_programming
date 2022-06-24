===========================
How to use 3-say_my_name.py
===========================

``say_my_name()`` prints My name is <first name> <last name>

::

	>>> say_my_name = __import__('3-say_my_name').say_my_name
	>>> say_my_name("Lynne", "Munini")
	My name is Lynne Munini

first_name and last_name must be strings otherwise, raise a TypeError.

::

	>>> say_my_name(1, "Munini")
	Traceback (most recent call last):
	TypeError: first_name must be a string

	>>> say_my_name("Lynne", 1)
	Traceback (most recent call last):
	TypeError: last_name must be a string

	>>> say_my_name(1, 1)
	Traceback (most recent call last):
	TypeError: first_name must be a string
