import os
import json

data = []

def get_json(file1):
    with open(file1) as f:
        for line in f:
            data.append(json.loads(line))

file1 = 'metadata_.json'
get_json(file1)

A = {}
for d in data:
    if not d.has_key('pdfPath'):
        continue
    pdf = d['pdfPath']
    pdf = pdf.split('/')
    a = len(pdf)
    if not A.has_key(a):
        A[a] = 1
    else:
        A[a] += 1

for a in A.keys():
    print str(a)+' '+str(A[a])


