lst = [1,2,3,3,4,5,6,7]

# How do you remove duplicates from an array in place?
def remove_duplicates(lst):
    track = []
    for i, e in enumerate(lst):
        if e in track:
            lst.pop(i)
        else:
            track.append(e)
    return lst
# print( remove_duplicates(lst) )


# How do you reverse an array in place?
def reverse(lst):
    for i in range( len(lst) // 2 ):
        lst[i], lst[-(i+1)] = lst[-(i+1)], lst[i]
    return lst
# print( reverse(lst) )


# How do you find the largest and smallest number in an unsorted integer array?
def find_max_min(lst):
    return {
        'smallest': min(lst),
        'largest': max(lst)
    }
# print( find_max_min(lst) )


#----------------------------------------------------------------------------

lst = [1,2,3,3,4,5,6,7]

# How do you remove duplicates from an array in place?
def remove_duplicates(lst):
    track = []
    for i, e in enumerate(lst):
        if e in track:
            lst.pop(i)
        else:
            track.append(e)
    return lst
# print( remove_duplicates(lst) )


# How do you reverse an array in place?
def reverse(lst):
    for i in range( len(lst) // 2 ):
        lst[i], lst[-(i+1)] = lst[-(i+1)], lst[i]
    return lst
# print( reverse(lst) )


# How do you find the largest and smallest number in an unsorted integer array?
def find_max_min(lst):
    return {
        'smallest': min(lst),
        'largest': max(lst)
    }
# print( find_max_min(lst) )
lst = [1,2,3,3,4,5,6,7]

# How do you remove duplicates from an array in place?
def remove_duplicates(lst):
    track = []
    for i, e in enumerate(lst):
        if e in track:
            lst.pop(i)
        else:
            track.append(e)
    return lst
# print( remove_duplicates(lst) )


# How do you reverse an array in place?
def reverse(lst):
    for i in range( len(lst) // 2 ):
        lst[i], lst[-(i+1)] = lst[-(i+1)], lst[i]
    return lst
# print( reverse(lst) )


# How do you find the largest and smallest number in an unsorted integer array?
def find_max_min(lst):
    return {
        'smallest': min(lst),
        'largest': max(lst)
    }
# print( find_max_min(lst) )
from random import randrange, randint
# https://assets.breatheco.de/apis/fake/zips.php

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


def mergesort(lst):
    if len(lst) < 2:
        return lst
    midpoint = len(lst)//2
    return merge(
        left = mergesort(lst[:midpoint]),
        right= mergesort(lst[midpoint:]) )


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