# This program uses re.sub() to transform or substitute strings that match a pattern.
# When matched, an action is taken like substituting string, invoking methods etc

# Sample input: if a + b > 0 && a - b < 0:

import re

def regSubstitution(match):
    if match.group(0) == ' && ':
        return ' and '
    else:
        return ' or '


if __name__=='__main__':
    n = int(input())
    pattern = "(\s&&\s | \s\|\|\s)"
    for _ in range(n):
        line = str(input())
        re.sub(pattern, regSubstitution, line)