import sys
import pickle
from WordBase import *
from Parser import Parser

# wb = WordBase()

# if not wb.load("wordBase.pck"):
# 	print("Error: file is not exists")
# 	exit(1)

# wb.print()

p = Parser()

p.parse()

for word in p.words:
	print(word.word)