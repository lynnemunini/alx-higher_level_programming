================================
How to use 5-text_indentation.py
================================

``text_indentation()`` prints a text with 2 new lines after each of . ? :

::

	>>> text_indentation = __import__('5-text_indentation').text_indentation
	>>> text_indentation("Hello world. My name is Lynne Munini")
	Hello world.
	<BLANKLINE>
	My name is Lynne Munini

text must be a string, otherwise raise a TypeError exception with the message text must be a string

::

	>>> text_indentation(222)
	Traceback (most recent call last):
	TypeError: text must be a string

	>>> text_indentation("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quonam modo: Utrum igitur tibi litteram videor an totas paginas commovere?")
	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
	<BLANKLINE>
	Quonam modo:
	<BLANKLINE>
	Utrum igitur tibi litteram videor an totas paginas commovere?
	<BLANKLINE>
