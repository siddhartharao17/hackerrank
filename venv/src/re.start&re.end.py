# This program uses the re module to match a substring k in a string S and if matched, returns the start and end indices

import re

def find_substring(k, S):
    # expression = "[a-z]+ | [a-zA-Z]+ | [a-zA-F0-9]+ | \d+"
    # regex = re.compile(expression, re.X)
    pattern = re.compile(k, re.X)
    isSubstring = pattern.search(S)
    if isSubstring == None:
        print("(-1, -1)")
    while isSubstring:
        print("(%d, %d)" % (isSubstring.start(), isSubstring.end()-1))
        isSubstring = pattern.search(S, pos=isSubstring.start()+1)

if __name__=='__main__':
    S = str(input('Enter the S string: '))
    k = str(input('Enter the k string: '))
    find_substring(k, S)