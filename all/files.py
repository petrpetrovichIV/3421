# try:
#     with open('img.png', 'rb') as img, open('img_copy.png', 'wb') as img_copy:
#         data = img.read()
#         img_copy.write(data)
#         print("File copies successfully")
# except FileNotFoundError:
#     print("File 'img.png' not found.")
#
# try:
#     with open('students.txt', 'r', encoding='utf-8') as source_file, open('backup.txt', 'w', encoding='utf-8') as backup:
#         students = source_file.read()
#         backup.write(students)
#         # students = file.readlines()
#         #
#         # num = 0
#         # for student in students:
#         #     num += 1
#         #     print(f'{num}) 🧑‍🎓 {student.strip()}')
# except FileNotFoundError:
#     print("File 'students.txt' not found.")

try:
    with open('students.txt', 'r', encoding='utf-8') as source_file:
        lines = source_file.readlines()

        count_lines = len(lines)
        count_words = 0
        count_chars = 0

        for line in lines:
            count_words += len(line.split(" "))
            count_chars += len(line)

        print(f'lines: {count_lines}\nwords: {count_words}\nchars: {count_chars}')

except FileNotFoundError:
    print("File 'students.txt' not found.")
#
# line = 'text text text. word word'
# print(len(line.split(" ")))

# try:
#     with open('students.txt', 'w', encoding='utf-8') as file:
#
#         new_student = input("Full Name: ")
#         file.write("\n" + new_student)
#
# except FileNotFoundError:
#     print("File 'students.txt' not found.")
# finally:
#     file.close()


# with open('','r') as source, open('','w') as backup:


# try:
#     with open('students.txt', 'r', encoding='utf-8') as file:
#         students = file.read()
#         print(students)
#         # students = file.readlines()
#         #
#         # num = 0
#         # for student in students:
#         #     num += 1
#         #     print(f'{num}) 🧑‍🎓 {student.strip()}')
# except FileNotFoundError:
#     print("File 'students.txt' not found.")