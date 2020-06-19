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