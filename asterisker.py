#!/usr/bin/env python
listFile = open('words.list', 'r', encoding='utf-8')
listFromFile = listFile.read().splitlines()

def repl(word, wordList):
	for i in wordList:
		asterisks = ''
		for j in range(len(i)):
			asterisks += '*'
		word = word.replace(i, asterisks)
	return word

while True:
	inWord = input('请输入文字:')
	if inWord == 'exit':
		break
	else:
		outWord = repl(inWord, listFromFile)
		print(outWord)
		print('')
