side = int(input("height: "))
symbol = input("symbol: ")

print(f"{symbol}\t" * side)
for _ in range(side - 2):
    print(f"{symbol}{'\t'*(side - 2)}\t{symbol}")
print(f"{symbol}\t" * side)