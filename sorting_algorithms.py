from time import time
from random import randrange

length = 100
lst = [randrange(length) for x in range(length)]


# BUBBLE SORT (time complexity: quadratic, linear)
# Time complexity is linear if when it goes thru it it's already
# sorted and the already_sorted flag kicks in.
# Takes the largest elements to the right on every iteration,
# stopping one item sooner every time
def bubble_sort(lst):
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
# print(bubble_sort(lst))


# INSERTION SORT (time complexity: quadratic, linear)
# Best for small lists.
# Time complexity is linear when the list is already sorted.
# Insertion sort is more efficient than bubble sort because in
# general it has to do less comparisons.
# Takes in each element from left to right, and inserts it
# left of the element starting right to left until it finds
# a smaller element
def insertion_sort(lst):
    for i in range(1, len(lst)):
        item = lst[i]
        j = i-1
        while j >= 0 and lst[j] > item:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = item
    return lst
# print(insertion_sort(lst))


# MERGE SORT
# Divide and conquer
def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    result = []
    ileft = iright = 0
    while len(result) < len(left) + len(right):
        if left[ileft] <= right[iright]:
            result.append(left[ileft])
            ileft += 1
        else:
            result.append(right[iright])
            iright += 1
        if iright == len(right):
            result += left[ileft:]
            break
        if ileft == len(left):
            result += right[iright:]
            break
    return result


length = 100000
lst1 = [x for x in range(length)]
lst2 = [x for x in range(length)]

times = []
for x in range(100):
    t = time()
    lst1 + lst2
    times.append(time()-t)
print('1#', sum(times)/100)

times = []
for x in range(100):
    t = time()
    [*lst1, *lst2]
    times.append(time()-t)
print('2#', sum(times)/100)
 
times = []
for x in range(100):
    t = time()
    [y for x in [lst1,lst2] for y in x]
    times.append(time()-t)
print('3#', sum(times)/100)
 
times = []
for x in range(100):
    new = [*lst1]
    t = time()
    new.extend(lst2)
    times.append(time()-t)
print('4#', sum(times)/100)


# k = [x for x in range(100000)]
# t = time()
# j = [x for x in k]
# print(time()-t)
# t = time()
# j = [*k]
# print(time()-t)