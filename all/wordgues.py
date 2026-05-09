import requests

# import random
# words = ["banana", "continue", "avocado", "zero", "seven", "pycharm"]
# word = random.choice(words)

while True:
    word = requests.get('https://random-word-api.herokuapp.com/word').json()[0]
    attempts = 0

    guessed = ['_'] * len(word)
    print(f' {' '.join(guessed)} ', end='')

    while True:
        attempts += 1
        try:

            l = input(f' gues[{attempts}]: ')[0]

            for i in range(len(word)):
                if word[i] == l:
                    guessed[i] = l

        except IndexError as ie:
            pass

        print(f' {' '.join(guessed)} ', end='')
        if ''.join(guessed) == word:
            break

    if input('Continue? Y/n').lower() == 'n':
        break