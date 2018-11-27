import re
import sys

intext = sys.stdin.read()

if re.search(r'佢', intext):
    print("I think this is Cantonese.")
else:
    print("I think this is Mandarin.")
