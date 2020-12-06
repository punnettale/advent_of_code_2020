batch_file = open("input4.txt","r").read().split("\n\n")

Documents = []

for ID in batch_file:
    doc = ID.split(" " and "\n")
    doc = [i.split(" ") for i in doc]
    doc = [j for i in doc for j in i]
    doc = [i.split(":") for i in doc]
    Documents.append(doc)

counter1 = 0
fields_needed = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
fields_needed_cid = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
Valid_Documents = []

for doc in Documents:
    if (len(doc) == 7):
        valid = True
        for stat in doc:
            if not ((stat[0] in fields_needed)):
                valid = False
        if valid == True:
            Valid_Documents.append(doc)
            counter1 += 1
    if (len(doc) == 8):
        valid = True
        for stat in doc:
            if not ((stat[0] in fields_needed_cid)):
                valid = False
        if valid == True:
            Valid_Documents.append(doc)
            counter1 += 1

counter2 = 0

for doc in Valid_Documents:
    valid = True
    for stat in doc:
        if stat[0] == "byr":
            if not ((1920 <= int(stat[1]) <= 2002) and (len(stat[1]) == 4)):
                valid = False
        elif stat[0] == "iyr":
            if not ((2010 <= int(stat[1]) <= 2020) and (len(stat[1]) == 4)):
                valid = False
        elif stat[0] == "eyr":
            if not ((2020 <= int(stat[1]) <= 2030) and (len(stat[1]) == 4)):
                valid = False
        elif stat[0] == "hgt":
            if "cm" in stat[1]:
                hgt = int(stat[1].replace("cm",""))
                if not (150 <= hgt <= 193):
                    valid = False
            elif "in" in stat[1]:
                hgt = int(stat[1].replace("in",""))
                if not (59 <= hgt <= 76):
                    valid = False
            else:
                valid = False
        elif stat[0] == "hcl":
            if not ((len(stat[1]) == 7) and (stat[1][0] == "#") and all(x in "#0123456789abcdef" for x in stat[1])):
                valid = False
        elif stat[0] == "ecl":
            if not (stat[1] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                valid = False
        elif stat[0] == "pid":
            if not ((len(stat[1]) == 9) and all(x in "0123456789" for x in stat[1])):
                valid = False
    if valid == True:
        counter2 += 1

print(counter1)
print(counter2)
