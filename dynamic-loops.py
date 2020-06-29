salute = ['Hi','Hello']
name = [' John, ',' Tim, ']
question = ['how are you?','how you been?']

lst = [salute, name, question]


def loop(lst, vars=''):
    if lst == []:
        print(vars)
        return

    copylst = [*lst]
    for x in copylst.pop(0):
        loop(copylst, vars+x)

loop(lst)

# for x in lst[0]:
#     for y in lst[1]:
#         for z in lst[2]:
#             print(x+y+z)