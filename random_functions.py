# How do you remove duplicates from an array in place?
lst = [1,2,3,3,4,5,6]

def remove_duplicates(lst):
    track = []
    for i, e in enumerate(lst):
        if e in track:
            lst.pop(i)
        else:
            track.append(e)
    return lst

print( remove_duplicates(lst) )