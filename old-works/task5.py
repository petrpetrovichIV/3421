a = int(input("num1: "))
b = int(input("num2: "))

start = min(a,b)
end = max(a,b)

d = 1
for i in range(start, end + 1):
    if i % 4 == 0 and i % 6 != 0:
        d = d * i

if d == 1:
    print("There are not such numbers!")
else:
    print(d)