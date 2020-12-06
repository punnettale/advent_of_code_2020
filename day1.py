import sys

numbers = open("input1.txt","r").read().splitlines()

#Part 1
for number in numbers:
    for num in numbers:
        if (float(number) + float(num) == 2020):
            print(float(number)*float(num))

#Part 2
for number in numbers:
    for num in numbers:
        for n in numbers:
            if (float(number) + float(num) + float(n) == 2020):
                print(float(number)*float(num)*float(n))
