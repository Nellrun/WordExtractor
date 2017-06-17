from Lexer import Lexer
from WordBase import Word

class Parser(object):
	"""docstring for Parser"""
	def __init__(self):
		self.lexer = Lexer()
		self.words = []

	def __error__(self, msg):
		print("Syntax error:", msg, "at line", self.lexer.lineNum, "column", self.lexer.columnNum)
		exit(1)

	def __sentence__(self):
		self.lexer.getLastLine()
		if self.lexer.sym == Lexer.SIGN or self.lexer.sym == Lexer.WORD or self.lexer.sym == self.lexer.NUM:
			words = []
			while self.lexer.sym != Lexer.NEWLINE:
				if self.lexer.sym == Lexer.WORD:
					words.append(self.lexer.value)
				self.lexer.nextTok()
			line = self.lexer.getLastLine()

			for word in words:
				self.words.append(Word(None, word, None, line))

			self.lexer.nextTok()
		else:
			self.__error__("word or sign expected")

	def __speeches__(self):
		while self.lexer.sym != Lexer.NEWLINE:
			self.__sentence__()
		self.lexer.nextTok()

		# if (self.lexer.sym != Lexer.NEWLINE):
		# 	self.__error__("new line expected")
		# else:
		# 	self.lexer.nextTok()

	def __time__(self):
		for i in range(3):
			if (self.lexer.sym != Lexer.NUM):
				self.__error__("number expected")
			self.lexer.nextTok()
			if i == 2:
				break
			if (self.lexer.sym != Lexer.COLON):
				self.__error__("colon expected")
			self.lexer.nextTok()

		if (self.lexer.sym != Lexer.COMMA):
			self.__error__("comma expected")

		self.lexer.nextTok()

		if (self.lexer.sym != Lexer.NUM):
			self.__error__("num expected")

		self.lexer.nextTok()

	def __timeLine__(self):
		self.__time__()

		if (self.lexer.sym != Lexer.ARROW):
			self.__error__("arrow expected")

		self.lexer.nextTok()

		self.__time__()

		if (self.lexer.sym != Lexer.NEWLINE):
			self.__error__("new line expected")

		self.lexer.nextTok()


	def __block__(self):
		if (self.lexer.sym != Lexer.NUM):
			self.__error__("id expected")

		self.lexer.nextTok()
		if (self.lexer.sym != Lexer.NEWLINE):
			self.__error__("new line expected")

		self.lexer.nextTok()
		self.__timeLine__()
		self.__speeches__()

	def parse(self):
		self.lexer.nextTok()

		while self.lexer.sym != Lexer.EOF:
			self.__block__()
		