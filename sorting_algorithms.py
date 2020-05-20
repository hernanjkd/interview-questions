from random import randrange

length = 100
lst = [randrange(length) for x in range(length)]


# BUBBLE SORT

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

# print(bubblesort(lst))

for x in range(5): print(x)