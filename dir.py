import os
import re
import csv

word = 'Tiru'
out=open("new_data.csv","wb")
output=csv.writer(out)
pattern=re.compile(r'[^-a-zA-Z0-9]%s[^-a-zA-Z0-9]' %(word))
rootDir = '/home/tiru/Desktop/tiru'
for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
    #print('Found directory: %s' % dirName)
    for fname in fileList:
       #print('\t%s' % fname)
       path=dirName+'/'+fname
       with open(dirName+'/'+fname, 'r') as f:
        for n,line in enumerate(f):
            if pattern.search(line):
                   # print 'found word: ', word, 'in line ', n
		   data = [[path,n,line]]
		   for row in data:
    			output.writerow(row)



out.close()
		   

      



