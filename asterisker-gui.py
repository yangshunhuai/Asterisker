#!/usr/bin/env python
from PySimpleGUI import *

listFile = open('words.list', 'r', encoding='utf-8')
listFromFile = listFile.read().splitlines()

def repl(word, wordList):
	for i in wordList:
		asterisks = ''
		for j in range(len(i)):
			asterisks += '*'
		word = word.replace(i, asterisks)
	return word

editButton = Button()

layout = []