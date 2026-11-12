with open("problems/problem-022/names.txt", "r") as file:
    names = sorted(file.read().replace("", '').split(','))

name_sum = 0

for i in range(len(names)-1):
    letter_sum = 0

    for letter in names[i]:
        letter_sum += ord(letter) - 64

    name_sum += (i+1)*letter_sum

print(name_sum)