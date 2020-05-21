from time import time

# COPY LIST
# spread   0.002324638366699218
# copy     0.002437300682067871
# loop     0.006635272502899170

# MERGE LISTS
# extend   0.002627000808715820
# plus     0.007303426265716553
# spread   0.007923214435577393
# loop     0.013505153656005860
# append   0.022672314643859864

'''
length = 100000
lst1 = [x for x in range(length)]
lst2 = [x for x in range(length)]

times = []
for x in range(100):
    t = time()
    lst1 + lst2
    times.append(time()-t)
print('1#', sum(times)/100)
# 0.007303426265716553

times = []
for x in range(100):
    t = time()
    [*lst1, *lst2]
    times.append(time()-t)
print('2#', sum(times)/100)
# 0.007923214435577393

times = []
for x in range(100):
    t = time()
    [y for x in [lst1,lst2] for y in x]
    times.append(time()-t)
print('3#', sum(times)/100)
# 0.01350515365600586
 
times = []
for x in range(100):
    new = [*lst1]
    t = time()
    new.extend(lst2)
    times.append(time()-t)
print('4#', sum(times)/100)
# 0.0026270008087158204

times = []
for x in range(100):
    new = [*lst1]
    t = time()
    for y in lst2:
        new.append(y)
    times.append(time()-t)
print('5#', sum(times)/100)
'''

'''
k = [x for x in range(100000)]
times = []
for x in range(100):
    t = time()
    [x for x in k]
    times.append(time()-t)
print('loop',sum(times)/100)
# 0.006611382961273194

times = []
for x in range(100):
    t = time()
    [*k]
    times.append(time()-t)
print('spread',sum(times)/100)
# 0.0023246383666992187
 
times = []
for x in range(100):
    t = time()
    k.copy()
    times.append(time()-t)
print('copy',sum(times)/100)
# 0.0024373006820678712
'''