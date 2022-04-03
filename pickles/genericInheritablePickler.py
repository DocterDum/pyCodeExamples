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
		atexit.register(self.save)
	
	def save(self):
		pickle.dump(self, open(self.pickleFileName, "wb"))
	
	@staticmethod
	def fromPickle(pickleFileName):
		self = pickle.load(open(pickleFileName, 'rb'))
		self.registerSave()
		return self

pickleFileName = 'test.pkl'
try:
	p = pickleable.fromPickle(pickleFileName)
except:
	p = pickleable(pickleFileName=pickleFileName)