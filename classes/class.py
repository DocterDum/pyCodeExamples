
# Create a class
class demoClass:
	pass

# Create an object (Instance of a class)
a = demoClass()

# Methods
# Methods are simply functions that are associated with a class
# By default methods are passed 'self' as an argument
# self refers to the instance of the class
# For the demo above, the 'c' variable contains the instance
class demoClassWithMethod:
	def demoMethod(self):
		print('demoMethod was run')

b = demoClassWithMethod()
b.demoMethod()

# Arguments for classes are defined in __init__
# __init__ is called the constructor for the class
# 
# Python automatically passes self to the __init__ method when it is called
class argDemo():
	def __init__(self, firstArg, kwArg = 'Default Value'):
		self.savedArg = firstArg
		print(kwArg)