import random

def check(a:int, b:int, c:int):
    return  a * b == c

crystals = 0

while True:
    a = random.randint(2,9)
    b = random.randint(2, 9)

    c = input(f'{a} x {b} = ')

    if check(a,b,int(c)):
        crystals += 1
    else:
        crystals -= 1

    print(f'💎 {crystals}')