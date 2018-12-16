# Consider the following:
#
#     A string,s, of length n where
# .     s = C0C1C2...Cn-1
# An integer, k, where k is a factor of n
#
#     .
#
# We can split s
# into n/k subsegments where each subsegment, Ti, consists of a contiguous block of k characters in s. Then, use
# each Tito create string Ui
#
# such that:
#
#     The characters in Ui
#
# are a subsequence of the characters in Ti
# .
# Any repeat occurrence of a character is removed from the string such that each character in Ui
# occurs exactly once. In other words, if the character at some index j in T occurs at a previous
# index < j in Ti, then do not include the character in string Ui
#
#     .
#
# Given s and k, print n/k lines where each line i denotes string Ui
#
# .
#
# Input Format
#
# The first line contains a single string denoting s
# .
# The second line contains an integer k,
# denoting the length of each subsegment.
#
# Constraints
#
# 1<= n <= 10^4, where n is the length of s.
# 1 <= k <= n
# It is guaranteed that is a multiple of
#
# Output Format
#
# Print n/k lines where each line i contains string Ui
#
# .
#
# Sample Input
#
# AABCAAADA
# 3
#
# Sample Output
#
# AB
# CA
# AD
#
# Explanation
#
# String s is split into n/k = 9/3 = 3 equal parts of length k = 3.
# We convert each Ti to Ui by removing any subsequent occurrences non-distinct characters in Ti
#
# 1. T0 = "AAB" --> U0 = "AB"
# 2. T1 = "CAA" --> U1 = "CA"
# 3. T2 = "ADA" --> U2 = "AD"
#
# We then print each Ui on a new line.


def dedup(subs):
    uniq = []
    for a in subs:
        # print(a)
        if a not in uniq:
            uniq.append(a)
    return ''.join(uniq)

def main():
    s = input()
    k = int(input())
    t = int(len(s) / k)

    for i in range(t):
        print(dedup(s[k*i:k*(i+1)]))

if __name__ == '__main__':
    main()