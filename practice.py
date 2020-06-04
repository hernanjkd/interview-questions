from random import randrange, randint


def issorted(lst):
    for i in range( len(lst)-1 ):
        if lst[i] > lst[i+1]:
            return False
    return True

def test_sort(func):
    length = 50
    lst = [randrange(length) for x in range(length)]
    while issorted(lst):
        lst = [randrange(length) for x in range(length)]
    copylst = [*lst]
    sortedlst = func(lst)
    assert issorted(sortedlst), \
        f'{func.__name__} [{",".join([str(x) for x in sortedlst])}]'



def insertionsort(lst):
    for i in range(1, len(lst)):
        item = lst[i]
        j = i-1
        while j >=0 and lst[j] > item:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = item
    return lst

test_sort(insertionsort)


def selectionsort(lst):
    n = len(lst)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if lst[j] < lst[min]:
                min = j
        if min != i:
            lst[i], lst[min] = lst[min], lst[i]
    return lst

test_sort(selectionsort)


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

test_sort(bubblesort)