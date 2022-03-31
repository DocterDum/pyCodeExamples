

# Descriptors can be used to inject behavior without affecting an interface
# Imagine you're currently running a library with a class 'cup'
# The users of your library will read the cups contents

# Our Library
class cup:
	def __init__(self, contents=None):
		self.contents = contents

# External user code
# User would import cup
def userCode(contentType: str):
	return cup(contents=contentType).contents

print('The user\'s function works:', userCode('Coffee'))

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
print('You broke the user\'s function by changing contents to a method:', userCode('Tea'))

# We can fix this using a descriptor:
class accessLogger:
	def __get__(self, obj, objtype=None):
		obj.logRead()
		return obj._value
	
	def __set__(self, obj, value):
		obj._value = value

class cup:
	contents = accessLogger()
	
	def __init__(self, contents=None):
		self.contents = contents # -> Calls accessLogger.__set__(self, contents)
	
	def logRead(self):
		pass

t = cup(contents='Coffee')
print('The old user code works again: ', userCode('Chai'))

# Properties are a more succinct way of creating a getter/setter that's unique to a single class:
# In this example _contents could be entirely renamed, this is just a common way to represent variable wrapped by a getter/setter
class cup:
	def __init__(self, contents=None):
		self._contents = contents
	
	def logRead(self):
		pass
	
	@property
	def contents(self):
		self.logRead()
		return self._contents
	
	@contents.setter
	def contents(self, value):
		self._contents = value

print('The code still works with a property: ', userCode('Milkshake'))
