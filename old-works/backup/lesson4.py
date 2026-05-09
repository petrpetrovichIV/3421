# Список запитань
truth_questions = [
    "Яку гру ти любиш найбільше і чому?",
    "Чи бувало, що ти підглядав/підглядала відповіді під час тесту?",
    "Який твій найсмішніший фейл у комп’ютерній грі?",
    "Чи ставив/ставила ти колись своїй команді 'трольний' код у проекті?",
    "Хто з твоїх друзів найсмішніше грав у Minecraft/Roblox?",
    "Який твій секрет у використанні комп’ютера (лайфхак або хитрість)?",
    "Чи коли-небудь ображав/ображала когось онлайн, а потім шкодував/шкодувала?",
    "Який твій найбільший страх у кіберпросторі (віруси, помилки, лаги)?",
    "Яку програму або гру ти мрієш створити?",
    "Чи траплялося тобі випадково видалити важливий файл?"
]

# Список дій
dare_actions = [
    "Намалюй на дошці свій улюблений персонаж з гри за 30 секунд.",
    "Склади невеличкий вірш або риму про комп’ютер.",
    "Покажи друзям свою 'танцювальну' позу геймерського переможця.",
    "Постав смішне фото у профіль на 10 хвилин.",
    "Придумай нову назву для комп’ютерної академії і проговори її вголос.",
    "Зроби 10 присідань, вимовляючи 'код написаний правильно'.",
    "Придумай коротку рекламу для своєї улюбленої гри і скажи її всім.",
    "Вигукай смішний крик перемоги геймера.",
    "Зімітуй свій улюблений баг у грі.",
    "Попроси друга надіслати тобі смішний мем у чат, а потім покажи його всім."
]

import random

def add_players(players:list):
    while True:
        name = input("name: ")
        if len(name) <= 2:
            continue

        players.append(name)

        if len(players) >= 2:
            choice = input("add one more player? (Y/n) ").lower()
            if choice == "y":
                continue
            else:
                break

players = []

add_players(players)

print(f'Players: {players}')

def game(players:list):
    while True:
        for player in players:
            print(f'Player {player}, please choose: ')
            choose = input("Q(?) or A(!) ").lower()

            if choose == 'q':
                index = random.randint(0,len(truth_questions)-1)
                print(f'(Q?) - {truth_questions[index]}')
                truth_questions.pop(index)
            elif choose == 'a':
                index = random.randint(0, len(dare_actions) - 1)
                print(f'(A!) - {dare_actions[index]}')
                dare_actions.pop(index)
            else:
                index = random.randint(0, len(truth_questions) - 1)
                print(f'(Q?) - {truth_questions[index]}')
                truth_questions.pop(index)

                index = random.randint(0, len(dare_actions) - 1)
                print(f'(A!) - {dare_actions[index]}')
                dare_actions.pop(index)

        next = input("==== NEXT TURN? Y/n ====").lower()
        if next != 'y':
            break

game(players)