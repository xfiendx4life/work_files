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

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

p = sys.argv[1]
var = sys.argv[2]

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
elif var == '-d':
	for item in fileList:
		textList.append(get_text(item))
	for i in range(len(textList)):
		for j in range(i + 1, len(textList)):
			print(similar(textList[i],textList[j]))

