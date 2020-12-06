list_raw = open("input2.txt","r").read().splitlines()
list_split = [i.split() for i in list_raw]
list_clean = [[i[0].split("-"),i[1].replace(":",""),i[2]] for i in list_split]

counter = 0

for i in list_clean:
    if i[2].count(i[1]) in range(int(i[0][0]),int(i[0][1]) + 1):
        counter += 1

print(counter)

counter = 0

for i in list_clean:
    lower = int(i[0][0]) - 1
    upper = int(i[0][1]) - 1
    password = i[2]

    if (password[lower] == i[1]) and (password[upper] == i[1]):
        pass
    elif (password[lower] == i[1]):
        counter += 1
    elif (password[upper] == i[1]):
        counter += 1
    else:
        pass

print(counter)
