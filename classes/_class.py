def endSection():
	print(' ')

# Create a class
from ast import arg


class demoClass:
	pass

# Create an object (Instance of a class)
a = demoClass()

# Methods
# Methods are simply functions that are associated with a class
# Python automatically passes self to methods when they are called
# self refers to the instance of the class
# For the demo above, the 'a' variable contains the instance
class demoClassWithMethod:
	def demoMethod(self):
		print('demoMethod was run')

b = demoClassWithMethod()
b.demoMethod()

endSection()

# Arguments for classes are defined in the __init__ method
# __init__ is called the constructor for the class
# Arguments passed to a class are usually stored - e.g. in the below example: 'self.savedArg = firstArg'
# This isn't always the case though, they can be used for other things as well, in this example kwArg is just printed and is never accessible again
class argDemo():
	def __init__(self, firstArg, kwArg = 'Default kwArg Value'):
		self.savedArg = firstArg
		print(kwArg)

c = argDemo('exampleFirstArg')
d = argDemo('otherFirstArg on a separate instance', kwArg='A different kwArg value')
print(c.savedArg)
print(d.savedArg)
try:
	print(d.kwArg)
except:
	print('d.kwArg was not stored and no longer exists')

endSection()

# A quick note on _
# Similar to for loops using _ for unused variables:
for _, i in zip(range(3,10), range(6,13)):
	not(i) # _ variable is not used

# An _ before a method name suggests it's not supposed to be called externally:
class fragileMethod:
	def __init__(self) -> None:
		self.storedValue = 0
	
	def _storeValue(self, value):
		self.storedValue = value
	
	def storeValue(self, value):
		if value < 5:
			pass
		else:
			self._storeValue(value)

e = fragileMethod()
e.storeValue(3) # Error checking prevents this from happening
print(f'The storeValue function prevented the small number from being stored: {e.storedValue}')
e._storeValue(3) # The error checking is never run and the value is stored
print(f'The _storeValue function doesn\'t prevent this: {e.storedValue}')