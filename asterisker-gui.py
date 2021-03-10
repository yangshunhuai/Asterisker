#!/usr/bin/env python
from PySimpleGUI import *
import os
import sys

platform = sys.platform
Print('Platform: ' + platform)

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
	if event == 'editFile':
		if platform == 'win32':
			os.system('notepad words.list')
	if event == WIN_CLOSED:
		break
root.close()