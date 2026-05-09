import random

num = random.randint(0,100)
guess = -1

attempt = 0

while num != guess:
    attempt += 1

    guess = int(input("guess: "))

    if (guess > num):
        print(f"{guess} > num")
    elif (guess < num):
        print(f"{guess} < num")
    else:
        print(f"Congratulations!!!👍 You guessed for {attempt} attempts.")