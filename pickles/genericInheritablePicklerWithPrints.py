import pickle
import atexit

class pickleable:
	def __init__(self, *args, **kwargs) -> None:
		try:
			self.pickleFileName = kwargs.pop('pickleFileName')
		except KeyError:
			raise KeyError('Please provide a pickle file name')
		self.registerSave()
	
	def registerSave(self):
		'''Registers {self.save} to run with atexit 
		'''
		atexit.register(self.save)
	
	def save(self):
		'''Pickles {self} to file named {self.pickleFileName}
		'''
		print('Saving Pickle')
		pickle.dump(self, open(self.pickleFileName, "wb"))
	
	@staticmethod
	def fromPickle(pickleFileName):
		self = pickle.load(open(pickleFileName, 'rb'))
		self.registerSave()
		return self

pickleFileName = 'test.pkl'
try:
	print('Loading Pickle')
	p = pickleable.fromPickle(pickleFileName)
	print('Loaded Pickle')
except:
	print('Load Failed, Creating New Object')
	p = pickleable(pickleFileName=pickleFileName)
	print('Loaded Object')
### Notice that even after loading the pickled object, it re-registers to again save on exit