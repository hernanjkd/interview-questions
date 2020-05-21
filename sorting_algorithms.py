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
# quick 0.06157848358154297
# inser 0.1027791714668274
# merge 0.16664746761322022
# bubbl 0.23856120586395263

length = 100
lst = [randrange(length) for x in range(length)]


# BUBBLE SORT (time complexity: quadratic, linear)
# Time complexity is linear if when it goes thru it it's already sorted and the
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

def mergesort(lst):
    if len(lst) < 2:
        return lst
    midpoint = len(lst)//2
    return merge(
        left = mergesort(lst[:midpoint]),
        right= mergesort(lst[midpoint:])
    )



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




def timesort(func, lst):
    times = []
    for x in range(100):
        arr = [*lst]
        t = time()
        func(arr)
        times.append(time()-t)
    return sum(times)/100

print('bubbl',timesort(bubblesort, lst))
print('inser',timesort(insertionsort, lst))
print('merge',timesort(mergesort, lst))
print('quick',timesort(quicksort, lst))