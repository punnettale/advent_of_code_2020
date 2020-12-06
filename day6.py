import string

declarations = open("input6.txt").read().split("\n\n")
declarations = [dec.splitlines() for dec in declarations]

alphabet = list(string.ascii_lowercase)
counter1 = 0
merged_lists = []

for dec in declarations:
    merged = "".join(dec)
    merged_lists.append(merged)

for decs in merged_lists:
    for letter in alphabet:
        if letter in decs:
            counter1 += 1

counter2 = 0

for dec in declarations:
    for letter in alphabet:
        valid = False
        for ans in dec:
            if letter in ans:
                valid = True
            elif letter not in ans:
                valid = False
                break
        if valid == True:
            counter2 += 1
        elif valid == False:
            pass

print(counter1)
print(counter2)
