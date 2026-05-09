import os

path = input('Path: ')

file_list = []

matcher = input("find: ")

for paths, dirs, files in os.walk(path):

    for file in files:
        if file.endswith(matcher):
            file_list.append(file)
            print(f'{file}')

if len(file_list) == 0:
    print(f"Any files with '{matcher}' not found!")
    exit()

print(f'We found {len(file_list)} file(s).')

with open('results.txt', 'w', encoding='utf-8') as file:

    file.write("\n".join(file_list))
























# last_name = input("last name: ")
# first_name = input("first name: ")
# patronymic = input("patronymic: ")
#
# city_from = input("city from:")
# city_to = input("city to:")
#
# date = input("date: ")
#
# content = f'Ticket #124 from {city_from} --> {city_to} [{date}]\n Owner: {last_name} {first_name} {patronymic}.'
#
# with open('ticket.txt', 'w', encoding='utf-8') as file:
#
#     print(file.write(content))
#
# print(f'Ticket was saved in {file}')
#
# file.close()