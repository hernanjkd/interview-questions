from random import randrange

length = 100
lst = [randrange(length) for x in range(length)]


# BUBBLE SORT

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

def insertion_sort(lst):
    for i in range(1, len(lst)):
        item = lst[i]
        j = i-1
        while j >= 0 and lst[j] > item:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = item
    return lst

print(insertion_sort(lst))