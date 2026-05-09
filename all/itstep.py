from prettytable import PrettyTable

table = PrettyTable(["No.","Surname", "Firstname", "Count Scores",  "Avg Score"])

with open('students.txt', 'r', encoding='utf-8') as students_file:

    students_lines = students_file.readlines()
    count_students = len(students_lines)
    sum_total = 0
    count_total = 0
    student_no = 1
    for student in students_lines:

        data = student.split(" ")

        sum = 0
        count = 0
        for i in range(2,len(data)):
            count += 1
            sum += int(data[i])

        count_total += count
        avg_score = sum/count
        sum_total += avg_score

        table.add_row([student_no, data[0], data[1], count, round(avg_score,1)])
        student_no += 1

    print(table)

    print(f'Total AVG score ({count_total}): {sum_total/count_students:.2f}')