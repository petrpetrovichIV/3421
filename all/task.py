with open('numbers.txt', 'r') as num_file, open('sum.txt', 'w') as sum_file:
    sum = 0
    for line in num_file.readlines():
        list = line.split(" ")
        for i in list:
            sum += int(i)

    print(f'sum: {sum}')
    sum_file.write(str(sum))