import random
#          0    1   2  3  4  5  6
scores = [1, 2, 3, 4, 5, 6, 7]
#         -7  -6   -5 -4 -3 -2 -1

# print(scores[random.randint(0, len(scores)-1)])

# for i in range(len(scores)):
#     print(f'scores[{i}]={scores[i]}')

total = 0
for score in scores:
    total += score
    print(score, end=" + ")

print(total)