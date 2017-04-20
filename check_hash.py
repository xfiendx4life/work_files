#!/usr/bin/python
import sys
import hashlib
import os

fileList = []
hashList = []
def get_hash_md5(filename):
    with open(filename, 'rb') as f:
        m = hashlib.md5()
        while True:
            data = f.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

p = sys.argv[1]
for path, subdirs, files in os.walk(p):
	for filename in files:
		f = os.path.join(path, filename)
		fileList.append(f)
for item in fileList:
	hashList.append(get_hash_md5(item))
for i in range (len(hashList)-1):
	for j in range(i+1,len(hashList)):
		if hashList[i]== hashList[j]:
			print(fileList[i] + '\n' + fileList[j])