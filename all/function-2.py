def dob(a,b):
    d = 1
    if a > b:
        tmp = a
        a = b
        b = tmp

    for i in range(a, b+1):
        d *= i

    return d

def dov_v2(a,b):
    d=1
    for i in range(min(a,b), max(a,b)+1):
        d *= i

    return d


print(dob(5,1))
print(dov_v2(5,1))

def fun_max(list_nums):
    max = list_nums[0]
    for i in list_nums:
        if i > max:
            max = i

    return max


print(fun_max([1,2,33,4,5,6,77]))
print(max([1,2,33,4,5,6,77]))

import random

def rand(a,b):
    return random.randint(min(a,b),max(a,b))

print(rand(10,1))