import sys
import pickle
from WordBase import *
from SentenceLexer import SentenceLexer
import re

if len(sys.argv) < 2:
	print("<program name> <subtitles file>")
	exit(1)

wb = WordBase()

if not wb.load("wordBase.pck"):
	print("Error: file is not exists")
	exit(1)

wb.statistic()

text = ""

for path in sys.argv[1:]:
	f = open(path, "r")
	lines = f.readlines()
	f.close()

	for line in lines:
		searchRes = re.search("^\\D.+", line)
		if searchRes != None:
			text += searchRes.group(0).strip()

	# sentences = re.split("(\. | \! | \?)", text)
	sentences = text.replace("!", ".").replace("?", ".").split(".")

	wordList = []

	for sentence in sentences:
		words = SentenceLexer(sentence).parse()
		for word in words:
			w = Word(None, word.strip(), None, " ".join(words))
			if not wb.contain(w):
				wordList.append(w)

	newWordList = WordBase()

	print("{} new words".format(len(wordList)))

	for word in wordList:
		if not newWordList.contain(word):
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

	# file = open(path + ".txt", "w")

	# for word in newWordList.words:
	# 	if (word.translate != None):
	# 		file.write(word.word + "\t" + word.translate + "\t" + word.sentense + "\n")
	# 	else:
	# 		file.write(word.word + "\t None \t" + word.sentense + "\n")

	# file.close()