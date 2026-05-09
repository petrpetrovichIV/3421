file_path = input('File path: ')
word = input('Word: ')

count = 0
with open(file_path, 'r') as file:
    for line in file.readlines():
        words = line.split(" ")
        for w in words:
            if w.lower() == word.lower():
                count += 1

print(f'I have found {count} word(s) "{word}" in a file {file_path}.')