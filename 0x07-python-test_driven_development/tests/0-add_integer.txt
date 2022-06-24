===========================
How to use 0-add_integer.py
===========================

``add_integer()`` returns the sum of its arguments.

::

	>>> add_integer = __import__('0-add_integer').add_integer
        >>> add_integer(100, 4)
        104
 
For floating-point values the values are first converted to integers.
 
::

	>>> add_integer(2.3, 3.2)
        5

Adding a floating-point value and an integer value.

::
	>>> add_integer(3.3, 3)
        6
 
First arguments must be an integer or float, otherwise TypeError exception is raised.
 
::
 
        >>> add_integer("yes", 6)
        Traceback (most recent call last):
        TypeError: a must be an integer

Second argument must be an integer or float, otherwise TypeError exception is raised.

::

        >>> add_integer(5, "girls")
        Traceback (most recent call last):
        TypeError: b must be an integer

Testing when both arguments are string literals

::

        >>> add_integer("yes", "girls")
        Traceback (most recent call last):
        TypeError: a must be an integer
