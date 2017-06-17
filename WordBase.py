import pickle

class Word(object):
	"""docstring for Word"""
	def __init__(self, id, word, translate, sentense):
		super(Word, self).__init__()
		self.id = id
		self.word = word
		self.translate = translate
		self.sentense = sentense

class WordBase(object):
	"""docstring for WordBase"""
	def __init__(self):
		super(WordBase, self).__init__()
		self.words = []

	"""appending <word> to end of list"""
	def append(self, word):
		self.words.append(word)

	"""Load words list from file with <filename>"""
	def load(self, filename):
		try:
			with open(filename, "rb") as f:
				self.words = pickle.load(f)
			return True
		except IOError:
			return False

	"""Save words to file with <filename>"""
	def save(self, filename):
		try:
			with open(filename, "wb") as f:
				pickle.dump(self.words, f)
			return True
		except IOError:
			return False;

	"""print <n> words in std::out"""
	def print(self, n = -1):
		for i, elem in enumerate(self.words):
			if (i != n):
				print(elem.word, elem.translate, elem.sentense, sep="\t")
		
	"""checking containing word in wordBase"""
	def contain(self, word):
		w = word.word.lower().strip()

		for word in self.words:
			if (w == word.word.lower().strip()):
				return True
		return False

	def statistic(self):
		print("Word base have", len(self.words), "words")