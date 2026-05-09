# while True:
#     try:
#         a = int(input("a: "))
#         print(5 / a)
#     except ZeroDivisionError as zd:
#         print(zd)
#     except ValueError as ve:
#         print(ve)

# try:
#     with open("tqext.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError as fne:
#     print(fne)

# def deposit():
#     amount = int(input("amount:"))
#     if amount >= 0:
#         print(f"+ ${amount}")
#     else:
#         raise ValueError("amount cannot be negative.")

# try:
#     deposit()
# except ValueError as ve:
#     print(ve)
# a = input("a: ")
#
# try:
#     print(a/5)
# except TypeError as te:
#     print(te)
#     try:
#         a = int(a)
#         print(a/5)
#     except ValueError as ve:
#         print(ve)
# import colorama
#
# dict = {
#     "user1": "10-12",
#     "user2": "11-12",
#     "user3": "13-14",
#     "user4": "15-16"
# }
#
# while True:
#     user = input("user_name: ")
#     try:
#         print(dict[user])
#     except KeyError as ke:
#         print(colorama.Fore.RED + f'User {ke} not found.' + colorama.Style.RESET_ALL)
#         try:
#             colorama.Style.random()
#         except AttributeError as ae:
#             print(ae)

result = []
def divider(a, b):
     if a < b:
        raise ValueError
     if b > 100:
        raise IndexError
     return a/b

data = {10:2, 2:5, "123": 4, 18: 0, 15:[], 8 : 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except TypeError as e:
        print(e)
    except ValueError as ve:
        print(ve)
    except ZeroDivisionError as zde:
        print(zde)


print(result)