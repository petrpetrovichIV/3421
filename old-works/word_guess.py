import random

fruit = ['banana', 'apple', 'pear', 'peach', 'orange', 'plum', 'grape', 'avocado']

guess_word = random.choice(fruit)
word = []
for _ in guess_word:
    word.append('_')

attempts = 0
while True:
    print(" ".join(word))

    alpha = input('gues: ')
    attempts += 1

    for i in range(len(guess_word)):
        if alpha == guess_word[i]:
            word[i] = alpha
    if "".join(word) == guess_word:
        print(f'You have won the game for {attempts} attempts.')
        if input("New game? Y/n ").lower() == 'n':
            break