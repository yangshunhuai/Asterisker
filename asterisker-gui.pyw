#!/usr/bin/env python
from PySimpleGUI import *
import os
import sys

platform = sys.platform
Print('系统平台: ' + platform)
Print('')

def loadFile():
	listFile = open('words.list', 'r', encoding='utf-8')
	listFromFile = listFile.read().splitlines()
	listFile.close()
	return listFromFile

def repl(word, wordList):
	for i in wordList:
		asterisks = ''
		for j in range(len(i)):
			asterisks += '*'
		word = word.replace(i, asterisks)
	return word

list1 = loadFile()
Print('脏话列表： ' + str(list1))

editButton = Button('修改列表文件', key='editFile')
loadButton = Button('刷新列表文件', key='reloadFile')
inText = Text('请输入文字')
inEntry = InputText(key='inWord')
inComplete = Button('开始过滤', key='start')

layout = [[editButton, loadButton], 
		 [inText, inEntry, inComplete]]

root = Window('Asterisker GUI', layout)

while True:
	event, values = root.read()
	if event == 'editFile':
		if platform == 'win32':
			os.system('editor\\bowpad.exe words.list')
		if platform == 'darwin' or platform == 'linux':
			os.system('vi words.list')
	if event == 'reloadFile':
		list1 = loadFile()
	if event == 'start':
		words = values['inWord']
		Print('原内容: ' + words)
		Print('')
		new = repl(words, list1)
		Print('现内容: ' + new)
		Print('')
	if event == WIN_CLOSED:
		break
root.close()
