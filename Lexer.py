import sys

class Lexer:
	COMMA, COLON, SIGN, EOF, NEWLINE, WORD, ARROW, NUM = range(8)

	SYMBOLS = {"," : COMMA, 
			   "." : SIGN, 
			   "!" : SIGN,
			   "?" : SIGN,
			   ":" : COLON,
			   "\"" : SIGN,
			   "_" : SIGN,
			   "\n" : NEWLINE}

	ch = " "
	sym = None
	value = None
	line = ""
	lineNum = 1
	columnNum = 0

	file = None

	def __init__(self, path):
		self.file = open(path, "r")

	def __error__(self, msg):
		print("Lexer error: ", msg, "at line", self.lineNum, "column", self.columnNum)
		exit(1)

	def __getc__(self):
		if (self.file == None):
			self.ch = sys.stdin.read(1)
		else:
			self.ch = self.file.read(1)

		self.line += self.ch

		self.columnNum += 1

		if (self.ch == "\n"):
			self.lineNum += 1
			self.columnNum = 0
		# print(self.ch)

	def getLastLine(self):
		line = self.line
		self.line = ""
		return line

	"""return next token in std::in"""
	def nextTok(self):
		self.sym = None
		self.value = None
		while self.sym == None:
			if len(self.ch) == 0:
				self.sym = Lexer.EOF
			elif self.ch == "\n":
				self.sym = Lexer.NEWLINE
				self.__getc__()
			elif self.ch.isspace():
				self.__getc__()
			elif self.ch in self.SYMBOLS:
				self.sym = self.SYMBOLS[self.ch]
				self.__getc__()
			elif self.ch == "-":
				self.__getc__()
				if self.ch != "-":
					self.sym = self.SIGN
				else:
					self.__getc__()
					if self.ch == ">":
						self.sym = self.ARROW
						self.__getc__()
					else:
						self.__error__("expected arrow \"-->\"")
			elif self.ch == "<":
				while self.ch != ">":
					self.__getc__()
				self.__getc__()
			elif self.ch.isdigit():
				value = ""
				while self.ch.isdigit():
					value += self.ch
					self.__getc__()
				self.sym = self.NUM
				self.value = value
			elif self.ch.isalpha():
				value = ""
				while self.ch.isalpha() or self.ch == "'":
					value += self.ch
					self.__getc__()
				self.sym = self.WORD
				self.value = value
			else:
				self.sym = self.SIGN
				self.__getc__()