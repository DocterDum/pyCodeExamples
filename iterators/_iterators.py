

# Iterators
# Iterators are classes which implement __iter__ and __next__
class iterator:
	def __iter__(self):
		self.last = 0
		return self
	
	def __next__(self):
		if self.last > 9:
			raise StopIteration()
		self.last += 1
		return self.last

results = []
for item in iterator():
	results.append(item)

print(results)

# The for loop above can be converted to use list comprehension:
results = [item for item in iterator()]
print(results)

# Iterators can be created using the yield keyword in a function instead
# These shortened versions are called generators
def iterFunc():
	for i in range(10):
		yield i

results = [item for item in iterFunc()]
print(results)

# The power of yield extends further than loops
# Any time we want to run code, hand off control, and then regain control later on, we can use yield.

# Imagine being a python module which requires three methods to be run in sequence:
class example:
	def first(self):
		print('first example')
	def second(self):
		print('second example')
	def third(self):
		print('third example')

# This is a candidate for running code, handing off control, and then returning control
# By chaining these together with yield, we can ensure they are called in the correct order:

def useExample():
	t = example()
	t.first()
	yield
	t.second()
	yield
	t.third()

print('first user')
a = useExample()
print('second user')
next(a)
print('third user')
next(a)
print('fourth user')
next(a)
print('fifth user')

# This example shows how yield can be used to enforce ordering while still allowing intermediate actions