'''
You are given a String S consisting of letters 'a' and 'b'. You want to split
it into three separate non empty parts. The lengths of the parts can differ
from one another

In how many ways can you split S into three parts, such that each part contains
the same number of letters 'a'?

Write a function:
    
    def solution(S)

that, given a string S of length N, return the number of possible ways of
splitting S as described above.

Examples:

1. "babaa" the function should return 2. The possible splits are:
"ba ba a" and "bab a a"

2. "ababa" the function should return 4. The possible splits are:
"a ba ba", "a bab a", "ab a ba" and "ab ab a"

3. "aba" the function should return 0.

4. "bbbbb" the function should return 6. The possible splits are:
"b b bbb", "b bb bb", "b bbb b", "bb b bb" and "bbb b b"
'''

def solution(S):
    N = len(S)
    if N < 1 or N > 40000 or N > (S.count('a') + S.count('b')):
        return 'Invalid input'

    lst = []
    for x in range(1, N-1):
        for y in range(2, N):
            if x >= y:
                continue
            temp = [ S[:x], S[x:y], S[y:] ]
            if same_a(temp):
                lst.append(temp)
    
    return len(lst)


def same_a(lst):
    count = None
    for x in lst:
        if count is None:
            count = x.count('a')
        if x.count('a') != count:
            return False
    return True

print(solution('babaa')) # correct answer 2
print(solution('ababa')) # correct answer 4
print(solution('aba')) # correct answer 0
print(solution('bbbbb')) # correct answer 6