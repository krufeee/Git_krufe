from termcolor import colored
from pyfiglet import figlet_format
# text = colored("krufee", "red", "on_white", attrs=["bold", "underline"])
# print(text)

text = colored(figlet_format('Figen'), "cyan", attrs=["bold"])
print(text, end="")


from modules_py import print_triangle
from modules_py.line import print_line

print_triangle()
print_line()