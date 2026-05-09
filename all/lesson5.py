from colorama import init, Fore, Back, Style

import colorama

help(colorama)

for method in dir(colorama):
    print(method)

init()

print(Fore.RED + 'This text is red')
print(Back.GREEN + 'And this has a green background'+ Style.RESET_ALL)
print(Style.BRIGHT + 'This text is bright'+ Style.RESET_ALL )
print('This text is back to normal')

# import requests
# import inspect
# import sys
#
# age = "12"
#
# print(requests.__name__)
#
# # for method in dir(requests):
# #     print(method)
#
# print(inspect.ismodule(requests))
# print(inspect.isfunction(requests.get))
#
# print(sys.argv)
# print(sys.path)
# print(sys.platform)
# print(sys.executable)
# print(sys.version)