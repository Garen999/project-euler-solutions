from string import ascii_uppercase

with open("names.txt") as file:
    names = file.read()

names.sort()

for name, ascii_letter in zip(names, ascii_uppercase):

