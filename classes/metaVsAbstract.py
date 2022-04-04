from abc import ABC, ABCMeta, abstractmethod

# Abstract base classes are used to define when a class should not be used to create objects
class MyABC(ABC): # This is the same as -> class MyABC(metaclass=ABCMeta):
	
	@abstractmethod
	def childMustOverride(self):
		pass
	
	def noNeedToOverrode(self):
		pass

class abcChild(MyABC):
	def childMustOverride(self):
		return super().childMustOverride()

try:
	instantiateMyABC = MyABC()
except:
	print('We cannot create instances of an ABC ')

try:
	instantiateabcChild = abcChild()
	print('But we can create instances of an ABC\'s children')
except:
	print('We shouldn\'t ever get an error')


# Indeed, metaclasses are especially useful to do black magic, and therefore complicated stuff. But by themselves, they are simple:
#  - intercept a class creation
#  - modify the class
#  - return the modified class

print('')
class MyMeta(type):
	def __new__(cls, name, bases, attributes, **kwargs):
		print('Run Custom Code Here __new__')
		print(name, bases, attributes, kwargs)
		return super().__new__(cls, name, bases, attributes, **kwargs)
	
	def __init__(self, *args, **kwargs):
		print('Run Custom Code Here __init__')
		super().__init__(*args, **kwargs)
	
	def __call__(self, *args, **kwargs):
		print('Run Custom Code Here __call__')
		return super().__call__(*args, **kwargs)

class metaChild(metaclass=MyMeta):
	def __new__(cls, *args, **kwargs):
		print('Child __new__')
		return super().__new__(cls, *args, **kwargs)
	
	def __init__(self, *args, **kwargs):
		print('Child __init__')
		super().__init__(*args, **kwargs)
	
	def __call__(self, *args, **kwargs):
		print('Child __call__')
		return super().__call__(*args, **kwargs)

test = metaChild()
# Notice that when this is run, we get the opportunity to run code before the class is created
# This is exactly how the ABC is implemented. Each @abstractmethod just marks the method with a flag
# It is expected that the child class (e.g. abcChild) overrides those methods, removing the flag
# When a child object is created, the metaclass (E.g. ABCMeta) is used to create the child, and the metaclass can check each method to ensure the flag is not set