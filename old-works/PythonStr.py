text = "Lorem Ipsum is simply dummy... Anerneb."

count = 0

for symbol in text:
    if symbol in ['.', '?', '!']:
        count += 1

print(f'We have found {count} sentences.')