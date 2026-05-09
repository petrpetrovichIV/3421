# a = int(input("a: "))
# n = int(input("n: "))
#
# sum = 0
# count = 0
# for i in range(a, n+1):
#     sum += i
#     count += 1
#
# print(f"sum={sum}")
# print(f"avg={sum/count}")

# 4! = 1 * 2 * 3 * 4 * 5
n = int(input("n: "))
res = 1
for i in range(1,n+1):
    res *= i
print(f"{n}! = {res}")
