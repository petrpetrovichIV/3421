line = input("Input string: ").lower()

print('Is palindrome') if line == line[::-1] else print('Is not palindrome')