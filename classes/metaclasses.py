### TODO: Multiple inheritance metaclass conflict
# https://stackoverflow.com/questions/28720217/multiple-inheritance-metaclass-conflict
#
# class A(B, C):
# 	pass
#
# -> If B and C both have metaclasses, Python cannot determine which metaclass A should use
#
#



# Imagine you're writing a library part of it relies on the users to define a method on a derived class:

# Library code
class base:
	def foo(self):
		return self.bar()

# User code
class derived(base):
	def bar(self):
		return 'bar'

# If the user fails to define the bar method, this will not cause an issue until the code is run