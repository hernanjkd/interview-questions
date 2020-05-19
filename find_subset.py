from pprint import pprint

# given a list find all the subsets that add up to a certain number
# for example: [2,4,6,10] -> 16

lst = [2, 4, 6, 10]
total = 16

subsets = []
def create_subset(lst, mem, index):
    if len(lst) == index:
        return
    
    x = lst[index]
    
    subset_with = [x, *mem]
    subset_without = [*mem]

    subsets.append( subset_with )
    
    create_subset(lst, subset_with, index+1)
    create_subset(lst, subset_without, index+1)



create_subset(lst, [], 0)

for sets in subsets:
    if sum(sets) == total:
        print('answer',sets)

        