class newExample:
	def __new__(cls):
		print('Before Creation')
		createdObject = super().__new__(cls)
		print('After Creation')
		return createdObject
t = newExample()
