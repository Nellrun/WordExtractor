import sys
import pickle
from WordBase import *


wb = WordBase()

if not wb.load("wordBase.pck"):
	print("Error: file is not exists")
	exit(1)

wb.print()