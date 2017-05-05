#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys
import hashlib
import os
from difflib import SequenceMatcher

fileList = []
hashList = []
textList = []
def get_hash_md5(filename):
    with open(filename, 'rb') as f:
        m = hashlib.md5()
        while True:
            data = f.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

def get_text(filename):
	with open(filename, encoding = "latin-1" ) as f:#!!!
		data = f.read()
	return data

def normalize(text):
	#text = text.replace('\n\n', '\n')
	return text.lower()

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
try:
	p = sys.argv[1]
	var = sys.argv[2]
	perc = int(sys.argv[3])

	for path, subdirs, files in os.walk(p):
		for filename in files:
			f = os.path.join(path, filename)
			fileList.append(f)

	if var == '-h':
		for item in fileList:
			hashList.append(get_hash_md5(item))
		for i in range (len(hashList)-1):
			for j in range(i+1,len(hashList)):
				if hashList[i]== hashList[j]:
					print(fileList[i] + '\n' + fileList[j])
					print("_______________________________")
	elif var == '-t':
		for item in fileList:
			textList.append(normalize(get_text(item)))
		for i in range(len(textList)):
			for j in range(i + 1, len(textList)):
				sim = similar(textList[i],textList[j])
				#print(sim)
				if sim >= perc/100:

					print(fileList[i] + '\n' + fileList[j] + '\n' + '--------%s' % sim)
					print("_______________________________")
	else:
		print("-h for hash checking, -t for text checking")
except:
	print('Error missed one parameter \n "-h" for hash checking, "-t" for text checking')