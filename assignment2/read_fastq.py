import sys

infile = sys.argv[1]

headers = []

with open(infile, 'r') as f:
    for line in f:
        if line.startswith('@'):
            headers.append(line.split('@')[1].strip('\n'))

print len(headers)
for i in headers:
    print i            
