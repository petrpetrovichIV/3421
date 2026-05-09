from prettytable import PrettyTable

# Specify column names while initializing the table
myTable = PrettyTable(["Student Name", "Class", "Section", "Percentage"])

# Add rows of data
myTable.add_row(["Leonard", "X", "B", "91.2 %"])
myTable.add_row(["Penny", "X", "C", "63.5 %"])
myTable.add_row(["Howard", "X", "A", "90.23 %"])
myTable.add_row(["Bernadette", "X", "D", "92.7 %"])
myTable.add_row(["Sheldon", "X", "A", "98.2 %"])

# Print the table
print(myTable)