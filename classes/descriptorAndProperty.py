

# Descriptors can be used to inject behavior without affecting an interface
# Imagine you're currently running a library with a class 'cup'
# The users of your library will read the cups contents

# Our Library
from importlib.resources import contents


class cup:
	def __init__(self, contents=None):
		self.contents = contents

# External user code
# User would import cup
def userCode():
	return cup(contents='Coffee').contents

print('The user\'s function works:', userCode())

# Now imagine you want update you library to log every time the user reads the contents:
class cup:
	def __init__(self, contents=None):
		self._contents = contents
	
	def logRead(self):
		pass
	
	def contents(self):
		self.logRead()
		return self._contents

# This implementation would break the previous user code as contents is now a function
print('You broke the user\'s function by changing contents to a method:', userCode())

# We can fix this using a descriptor:
class accessLogger:
	def __get__(self, obj, objtype=None):
		return obj._value
	
	def __set__(self, obj, value):
		obj._value = value

class cup:
	contents = accessLogger()
	
	def __init__(self, contents=None):
		self.contents = contents # -> Calls accessLogger.__set__(self, contents)

t = cup(contents='Coffee')
print('The old user code works again: ', userCode())

