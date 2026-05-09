import sqlite3
from tokenize import group

connection = sqlite3.connect("itstep.sl3")
cursor = connection.cursor()

# surname = input("name: ")'
# group_name = input("group: ")

# cursor.execute(f"SELECT * FROM students  WHERE FULL_NAME like '%{surname}%;")
# cursor.execute(f"SELECT * FROM students  WHERE Group_Name = '{group_name}';")
cursor.execute(f"SELECT * FROM students  WHERE avg_score >= 4.5 and CRYSTALS > 80;")
connection.commit()
for student in cursor.fetchall():
    print(student)

connection.close()