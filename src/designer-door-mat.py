#
# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
#
#     Mat size must be
#
# X. ( is an odd natural number, and is times
#
#     .)
#     The design should have 'WELCOME' written in the center.
#     The design pattern should only use |, . and - characters.
#
# Sample Designs
#
#     Size: 7 x 21
#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------
#
#     Size: 11 x 33
#     ---------------.|.---------------
#     ------------.|..|..|.------------
#     ---------.|..|..|..|..|.---------
#     ------.|..|..|..|..|..|..|.------
#     ---.|..|..|..|..|..|..|..|..|.---
#     -------------WELCOME-------------
#     ---.|..|..|..|..|..|..|..|..|.---
#     ------.|..|..|..|..|..|..|.------
#     ---------.|..|..|..|..|.---------
#     ------------.|..|..|.------------
#     ---------------.|.---------------
#
# Input Format
#
# A single line containing the space separated values of
# and
#
# .
#
# Constraints
#
# Output Format
#
# Output the design pattern.
#
# Sample Input
#
# 9 27
#
# Sample Output
#
# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------

def printDoorMat(numberofrows, maxcols):
    if (numberofrows%2 != 0) and (maxcols == numberofrows * 3):
        if numberofrows == 1:
            print('WELCOME')
            return
        else:
            str = '.|.'
            row = 0

            for row in range(int(numberofrows / 2)):
                print((str * (2 * row + 1)).center(maxcols, '-'))

            print('WELCOME'.center(maxcols, '-'))

            while row > -1:
                print((str * (2 * row + 1)).center(maxcols, '-'))
                row -= 1
    else:
        print('Bad input supplied!')

if __name__ == '__main__':
    inputArgs = input().split()
    numberofrows, maxcols = int(inputArgs[0]), int(inputArgs[1])
    printDoorMat(numberofrows, maxcols)
    # print(numberofrows)
    # print(maxcols)
