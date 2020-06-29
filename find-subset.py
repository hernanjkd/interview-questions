from pprint import pprint
from time import time

# given a list find all the subsets that add up to a certain number
# for example: [2,4,6,10] -> 16

# question to ask: can there be any zeros in the list?
# are the numbers in order?

# Conclusion, answer 2 takes half the time as answer 1
# because it only continues if there's a possibility to reach the target,
# if the sum overpasses the target it will stop

lst = [2, 4, 6, 10, 1, 3, 8, 7]
total = 16


# Answer 2
subsets = []
answer = 0
def create_subset(lst, mem=[], index=0):
    if len(lst) == index:
        return
    
    x = lst[index]
    
    subset_with = [x, *mem]
    subset_without = [*mem]

    subsets.append( subset_with )

    global answer
    
    w = sum(subset_with)
    if w == total:
        answer += 1
    elif w < total:
        create_subset(lst, subset_with, index+1)

    w = sum(subset_without)
    if w == total:
        answer += 1
    elif w < total: 
        create_subset(lst, subset_without, index+1)

t = time()
create_subset(lst)
print('answer 2',time() - t)
print('answer 2',answer)


# Answer 1
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


t = time()
create_subset(lst, [], 0)

answer = 0
for sets in subsets:
    if sum(sets) == total:
        answer += 1
print('answer 1',time() - t)
print('answer 1',answer)
        
