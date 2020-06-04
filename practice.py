from random import randrange, randint


def bubblesort(lst):
    n = len(lst)
    for i in range(n):
        already_sorted = True
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                already_sorted = False
        if already_sorted:
            break
    return lst

def issorted(lst):
    for i in range( len(lst)-1 ):
        if lst[i] > lst[i+1]:
            return False
    return True

def test_sort(func):
    lst = [randrange(3) for x in range(3)]
    while issorted(lst):
        print(lst)
        lst = [randrange(3) for x in range(3)]
    copylst = [*lst]
    sortedlist = func(lst)

test_sort()