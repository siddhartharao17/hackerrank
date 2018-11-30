# Consider a list (list = []). You can perform the following commands:
#
#     insert i e: Insert integer
#
# at position
# .
# print: Print the list.
# remove e: Delete the first occurrence of integer
# .
# append e: Insert integer
#
#     at the end of the list.
#     sort: Sort the list.
#     pop: Pop the last element from the list.
#     reverse: Reverse the list.
#
# Initialize your list and read in the value of
# followed by lines of commands where each command will be of the
#
# types listed above. Iterate through each command in order and perform the corresponding operation on your list.
#
# Input Format
#
# The first line contains an integer,
# , denoting the number of commands.
# Each line of the
#
# subsequent lines contains one of the commands described above.
#
# Constraints
#
#     The elements added to the list must be integers.
#
# Output Format
#
# For each command of type print, print the list on a new line.
#
# Sample Input 0
#
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
#
# Sample Output 0
#
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

starLst = []

def lstMethod(args):
    if args[0] == 'insert':
        starLst.insert(args[1], args[2])
    if args[0] == 'remove':
        starLst.remove(args[1])
    if args[0] == 'append':
        starLst.append(args[1])
    if args[0] == 'sort':
        starLst.sort()
    if args[0] == 'print':
        print(starLst)
    if args[0] == 'pop':
        starLst.pop()
    if args[0] == 'reverse':
        starLst.reverse()

def parseCommand(command):
    if len(command) == 1:
        lstMethod(command)
    else:
        # comman_name = command[0]
        for i in range(1, len(command)):
            command[i] = int(command[i])
        lstMethod(command)

if __name__ == '__main__':
    # list = []
    number_of_commands = int(input())
    for _ in range(number_of_commands):
        command = input().split(' ')
        parseCommand(command)