from time import time
from random import randrange, randint

# lst length 10
# inser 1.3074874877929688e-05
# bubbl 2.1622180938720703e-05
# quick 4.0788650512695315e-05
# merge 5.470514297485351e-05

# lst length 100
# bubbl 4.2753219604492186e-05
# inser 4.7523975372314456e-05
# quick 0.0005417561531066894
# merge 0.0010808634757995606

# lst length 10,000
# quick 0.06294780015945435
# times 0.1401864743232727
# merge 0.16730313062667845
# inser 9.771325569152832
# bubbl 23.391096591949463

length = 10
lst = [randrange(length) for x in range(length)]


# BUBBLE SORT (time complexity: quadratic, linear)
# Time complexity is linear when it goes thru it and it's already sorted and the
# already_sorted flag kicks in.
# Takes the largest elements to the right on every iteration, stopping one item
# sooner every time
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



# SELECTION SORT (time complexity: quadratic)
def selectionsort(lst):
    n = len(lst)
    min = None
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if lst[j] < lst[min]:
                min = j
        if min != i:
            lst[i], lst[min] = lst[min], lst[i]
    return lst



# INSERTION SORT (time complexity: quadratic, linear)
# Best for small lists.
# Time complexity is linear when the list is already sorted.
# Insertion sort is more efficient than bubble sort because in general it has 
# to do less comparisons.
# Takes in each element from left to right, and inserts it left of the element
# starting right to left until it finds a smaller element
def insertionsort(lst):
    for i in range(1, len(lst)):
        item = lst[i]
        j = i-1
        while j >= 0 and lst[j] > item:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = item
    return lst



# MERGE SORT (time complexity: logarithmic, for the merge func it's linear)
# Divide and conquer. Very efficient algorithm, faster for big lists,
# slower than bubble and insertion for small lists. Takes up too much mem.
# Halves the list until there's only one item, then merges all the lists.
def merge(left, right):
    

def mergesort(lst):
    if len(lst) < 2:
        return lst
    midpoint = len(lst)//2
    return merge(
        left = mergesort(lst[:midpoint]),
        right= mergesort(lst[midpoint:]) )



# QUICKSORT (time complexity: logarithmic)
# Divide and conquer. Divides the list into smaller same and larger elements
# comparing them to a pivot element chosen at random. It recursively keeps
# dividing the list and combining it until it's sorted
def quicksort(lst):
    if len(lst) < 2:
        return lst
    low, same, high = [], [], []
    pivot = lst[ randint(0, len(lst)-1) ]
    for x in lst:
        if x < pivot:
            low.append(x)
        elif x > pivot:
            high.append(x)
        elif x == pivot:
            same.append(x)
    return quicksort(low) + same + quicksort(high)



# TIMESORT
# The default Python sorting algorithm. It's the most efficient because it
# uses the best of both worlds, insertion for smaller sections and it merges
# them
def insertion(lst, left=0, right=None):
    if right is None:
        right = len(lst)-1
    for i in range(left+1, right+1):
        x = lst[i]
        j = i-1
        while j >= left and lst[j] > x:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = x
    return lst

def timesort(lst):
    min_run = 32
    n = len(lst)
    for i in range(0, n, min_run):
        insertion(lst, i, min((i+min_run-1), n-1))
    size = min_run
    while size < n:
        for start in range(0, n, size*2):
            midpoint = start + size - 1
            end = min((start+size*2-1), (n-1))
            merged_lst = merge(
                left = lst[start: midpoint+1],
                right = lst[midpoint+1: end+1] )
            lst[start: start+len(merged_lst)] = merged_lst
        size *= 2
    return lst




def time_algorithm(func, lst):
    times = []
    for x in range(100):
        arr = [*lst]
        t = time()
        func(arr)
        times.append(time()-t)
    return sum(times)/100

# print('bubbl',time_algorithm(bubblesort, lst))
# print('inser',time_algorithm(insertionsort, lst))
# print('merge',time_algorithm(mergesort, lst))
# print('quick',time_algorithm(quicksort, lst))
# print('times',time_algorithm(timesort, lst))

print( selectionsort(lst) )
