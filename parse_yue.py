import sys
from pprint import pprint

infilename = sys.argv[1]

with open(infilename, 'r') as f:
    inlines = f.readlines()

clean_lines = [i.rstrip() for i in inlines]
sep_lines = [i.split('\t') for i in clean_lines]

pprint(sep_lines)

dict = {}
for line in sep_lines:
    dict[line[1]] = [line[0], line[2]]

pprint(dict)
