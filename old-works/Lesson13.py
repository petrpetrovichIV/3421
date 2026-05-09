# a = int(input("a: "))
# b = input("b: ")
#
# for i in range(a+1):
#     print(" " * (a - i) + b * i)

a = int(input("a: "))
b = int(input("b: "))

s1 = input("s1: ")
s2 = input("s2: ")

for i in range(a):
    for j in range(b):
        if (i+j) % 2 == 0:
            print(f'{s1}', end="\t")
        else:
            print(f'{s2}', end="\t")
    print("")