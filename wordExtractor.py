import sys
import pickle
from WordBase import *
from Parser import Parser

if len(sys.argv) < 2:
	print("<program name> <subtitles file>")
	exit(1)

wb = WordBase()

if not wb.load("wordBase.pck"):
	print("Error: file is not exists")
	exit(1)

wb.statistic()

for path in sys.argv[1:]:
	p = Parser(path)
	p.parse()

	newWordList = WordBase()

	for word in p.words:
		if not wb.contain(word) and not newWordList.contain(word):
			print()
			print(word.word)
			print(word.sentense.strip())
			print("Do you know this word?[y/n]")
			answer = input()
			if (answer.lower() == "n"):
				newWordList.append(Word(None, word.word, None, word.sentense))
			else:
				wb.append(Word(None, word.word, None, word.sentense))

	wb.save("wordBase.pck")

	file = open(path + ".txt", "w")

	for word in newWordList.words:
		if (word.translate != None):
			file.write(word.word + "\t" + word.translate + "\t" + word.sentense + "\n")
		else:
			file.write(word.word + "\t None \t" + word.sentense + "\n")

	file.close()