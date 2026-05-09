line = input("Input string: ")

alpha = 0
digit = 0
symb = 0

for _ in line:
    if _.isalpha():
        alpha += 1
    elif _.isdigit():
        digit += 1
    else:
        symb += 1

print(f'in line is {alpha} symbols, digits is {digit}, others is {symb}')