class SentenceLexer(object):
	"""docstring for SentenceLexer"""

	SYMBOLS = [",", ".", "!", "?", ":", "_", "\n"]
	# SYMBOLS = {"," : COMMA, 
	# 		   "." : SIGN, 
	# 		   "!" : SIGN,
	# 		   "?" : SIGN,
	# 		   ":" : COLON,
	# 		   "\"" : SIGN,
	# 		   "_" : SIGN,
	# 		   "\n" : NEWLINE}

	def __init__(self, sentence):
		super(SentenceLexer, self).__init__()
		self.sentence = sentence
		self.__ch = ""
		self.ind = 0
		self.words = []

	def __getc(self):
		if (self.ind < len(self.sentence)):
			self.__ch = self.sentence[self.ind]
		else:
			self.__ch = ""

		self.ind += 1

	def parse(self):
		self.__getc()
		while self.__ch != "":
			if self.__ch.isspace():
				self.__getc()
			elif self.__ch in self.SYMBOLS:
				self.__getc()
			elif self.__ch.isdigit():
				self.__getc()
			elif self.__ch == "<":
				while self.__ch != ">":
					self.__getc()
				self.__getc()
			elif self.__ch.isalpha():
				word = ""
				while self.__ch.isalpha() or self.__ch == "-" or self.__ch == "\'":
					word += self.__ch
					self.__getc()
				if word.isupper():
					continue
				self.words.append(word)
			else:
				# print("unknow symbol {}".format(self.__ch))
				self.__getc()
		return self.words


		