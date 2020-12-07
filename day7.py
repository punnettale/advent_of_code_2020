import re

rules = open("input7.txt","r").read().splitlines()
rules = [re.split(" bags contain | bags, ", rule) for rule in rules]

for rule in rules:
    rule[-1] = rule[-1].replace(" bags.","")

    # Removing the numbers, may need to comment out for part 2
    '''
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in rule:
        for j in numbers:
            i = i.replace(j, "").strip()
    '''

bag_list = []
previous_set_length = -1

while previous_set_length != len(set(bag_list)):
    previous_set_length = len(set(bag_list))
    for rule in rules:
        for bag in rule:
            if "shiny gold" in bag and bag != rule[0]:
                bag_list.append(rule[0])
                container = rule[0]
            else:
                for i in bag_list:
                    if i in bag and bag != rule[0]:
                        bag_list.append(rule[0])

print(len(set(bag_list)))
