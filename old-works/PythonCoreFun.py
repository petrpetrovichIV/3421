import calc

a =  int(input("a: "))
op = input("op: ")
b =  int(input("b: "))

if op == "+":
    print(f'{a} + {b} = {calc.sum(a, b)}')
elif op == "-":
    print(f'{a} - {b} = {calc.dif(a, b)}')
elif op == "^":
    print(f'{a} ^ {b} = {calc.pow(a, b)}')
else:
    print("wrong operation ⚠️")