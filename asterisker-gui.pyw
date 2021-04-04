#!/usr/bin/env python
# Author:yangshunhuai@jzcj

from PySimpleGUI import *
import os
import sys

platform = sys.platform
# Print('系统平台: ' + platform)
# Print('')

def loadFile():
	global noFile
	if not os.path.isfile('words.list'):
		popup('没有找到words.list文件！Asterisker即将退出')
		noFile = True
	else:
		noFile = False
	listFile = open('words.list', 'r', encoding='utf-8')
	listFromFile = listFile.read().splitlines()
	listFile.close()
	return listFromFile

if not os.path.isfile('editor\\bowpad.exe'):
	popup('没有找到BowPad编辑器！编辑功能不可用！')
	global noEditor
	noEditor = True
else:
	noEditor = False

def repl(word, wordList):
	for i in wordList:
		asterisks = ''
		for j in range(len(i)):
			asterisks += '*'
		word = word.replace(i, asterisks)
	return word

def showOutput(rootWin, oldWord, newWord):
	oldWordText = Text('输入内容')
	inputMultiline = Multiline(default_text=oldWord)
	newWordText = Text('输出内容')
	outputMultiline = Multiline(default_text=newWord)
	backToMain = Button('回到主界面', key='back')
	outputLayout = [[oldWordText], 
					[inputMultiline],
					[newWordText],
					[outputMultiline], 
					[backToMain]]
	rootWin.Hide()
	outputWin = Window('显示输出', outputLayout)
	while True:
		event, values = outputWin.read()
		if event == 'back' or event == WIN_CLOSED:
			outputWin.close()
			rootWin.UnHide()
			break

def showLicense(rootWin, text):
	licenseMultiline = Multiline(default_text=text, size=(70,20))
	backToMain = Button('回到主界面', key='back')
	licenseLayout = [[licenseMultiline], 
					 [backToMain]]
	rootWin.Hide()
	licenseWin = Window('开源信息', licenseLayout)
	while True:
		event, values = licenseWin.read()
		if event == 'back' or event == WIN_CLOSED:
			licenseWin.close()
			rootWin.UnHide()
			break

list1 = loadFile()
# Print('关键词列表： ' + str(list1))

editButton = Button('修改列表文件', key='editFile')
loadButton = Button('刷新列表文件', key='reloadFile')
inText = Text('请输入文字', size=(10, 5))
inMultiline = Multiline(size=(30, 5), key='inWord')
inComplete = Button('开始过滤', size=(10, 5), key='start')
copyrightText1 = Text('Copyright (c) 2021 yangshunhuai')
copyrightText2 = Text('本程序依照 MIT 协议开源。')
copyrightButton = Button('查看开源信息', key='showLicense')

layoutMain = [[editButton, loadButton], 
		      [inText, inMultiline, inComplete], 
		      [copyrightText1], 
		      [copyrightText2, copyrightButton]]

root = Window('Asterisker GUI', layoutMain)

while True:
	event, values = root.read()
	if noFile:
		break
	if event == 'editFile' and not noEditor == True:
		if platform == 'win32':
			os.system('editor\\bowpad.exe words.list')
		if platform == 'darwin' or platform == 'linux':
			os.system('vi words.list')
	if event == 'reloadFile':
		list1 = loadFile()
	if event == 'start':
		words = values['inWord']
		# Print('原内容: ' + words)
		# Print('')
		new = repl(words, list1)
		# Print('现内容: ' + new)
		# Print('')
		showOutput(root, words, new)
	if event == 'showLicense':
		licenseFile = open('LICENSE', 'r', encoding='utf-8')
		licenseTxt = licenseFile.read()
		showLicense(root, licenseTxt)
	if event == WIN_CLOSED:
		break
root.close()
