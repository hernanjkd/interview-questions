# How do you remove duplicates from an array in place?
lst = [1,2,3,3,4,5,6,7]

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

print( reverse(lst) )
# lst[1], lst[-2] = lst[-2], lst[1]
# print(lst)