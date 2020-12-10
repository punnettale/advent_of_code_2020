import re

boot_code = open("input8.txt","r").read().splitlines()

def get_quantity(string):
    quantity = int(re.findall('\d+', string)[0])
    return quantity

line = 0
acc = 0
executed_lines = []

while acc == 0 or line not in executed_lines:

    executed_lines.append(line)
    current_line = boot_code[line]

    if "acc" in current_line:
        if "+" in current_line:
            acc += get_quantity(current_line)
        elif "-" in current_line:
            acc -= get_quantity(current_line)
        line += 1

    elif "jmp" in current_line:
        if "+" in current_line:
            line += get_quantity(current_line)
        elif "-" in current_line:
            line -= get_quantity(current_line)

    elif "nop" in current_line:
        line += 1

print(acc)
