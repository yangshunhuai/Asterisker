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

editButton = Button('修改列表文件', key='editFile')
inText = Text('请输入文字')
inEntry = InputText(key='inWord')

layout = [[editButton], 
		 [inText], [inEntry]]

root = Window('Asterisker GUI', layout)

while True:
	event, values = root.read()
