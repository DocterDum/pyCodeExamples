def endSection():
	print(' ')

# Class methods and Static methods are special forms of methods
# Class methods are created before the class is instantiated, and operate on cls instead of self
# Static methods are similar except they operate on neither cls or self
# Static methods are essentially normal functions just under the namespace of the class

# Class methods can be used to create alternate constructors:
class sumOf:
	def __init__(self, valuesToSum: list) -> None:
		assert type(valuesToSum) == list
		self.result = sum(valuesToSum)
	
	def __str__(self) -> str:
		return str(self.result)
	
	@classmethod
	def fromTuple(cls, valuesToSum):
		convertedToList = [x for x in valuesToSum]
		return cls(convertedToList)

listToSum = [1, 2, 3, 4]
tupleToSum = (1, 2, 3, 4)

print(f'Succeeds because the constructor accepts a list: {sumOf(listToSum)}')
try:
	sumOf(tupleToSum)
except:
	print('Failed because sumOf expects a list not a tuple')
print(f'Succeeds because the class method converts the tuple to a list: {sumOf.fromTuple(tupleToSum)}')

endSection()

# Static methods are uninteresting:
class dumbConcept:
	@staticmethod
	def dumbMethod():
		return 'This is dumb'

def lessDumbMethod():
	return 'This is less dumb'

print(dumbConcept.dumbMethod())
print(lessDumbMethod())