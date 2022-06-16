
class Example:
	""" A Generic Class """
	
	def __str__(self) -> str:
		return 'ExampleObject'
	
	def __format__(self, format_spec: str) -> str:
		# Prints format_spec just to show that it itself is a string
		print(f'{format_spec = }')
		return str(self)+' '+format_spec

# Create instance
e = Example()

# Using an fstring calls __format__ on all items inside each {}
print(f'{e:formatName}')

# __format__ can handle format specs however you like - The spec is just passed as a string