
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