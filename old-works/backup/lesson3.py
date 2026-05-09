import random

def game(user_choice, result:dict):

    print("======= START GAME 🪨✂️📜 =======")

    computer_choice = random.choice("rps")

    print(f'👨: {user_choice}\n🖥️: {computer_choice}')

    if user_choice == computer_choice:
        print("👨 == 🖥️")

    if user_choice == 'r' and computer_choice == 's':
        print('👨🏆 win')
        result["user"] += 1
    if user_choice == 'p' and computer_choice == 'r':
        print('👨🏆 win')
        result["user"] += 1
    if user_choice == 's' and computer_choice == 'p':
        print('👨🏆 win')
        result["user"] += 1

    if computer_choice == 'r' and user_choice == 's':
        print('🖥️🏆 win')
        result["pc"] += 1
    if computer_choice == 'p' and user_choice == 'r':
        print('🖥️🏆 win')
        result["pc"] += 1
    if computer_choice == 's' and user_choice == 'p':
        print('🖥️🏆 win')
        result["pc"] += 1

    print(f'\n👨 {result["user"]} vs 🖥️ {result["pc"]}')

result = {"user": 0, "pc": 0}
while True:
    user_choice = input("r/p/s: ")
    game(user_choice, result)