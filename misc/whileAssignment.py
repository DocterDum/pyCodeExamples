ts = [1, 2, 3, 4]

# list.pop returns IndexError if no items left
try:
	while t := ts.pop():
		print(t)
except IndexError:
	pass

