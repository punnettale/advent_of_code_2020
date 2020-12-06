import math

slope = open("input3.txt","r").read().splitlines()

slope_width = len(slope[0])
slope_height = len(slope)
position = [0, 0]
position_shifts = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

trees_hit = []
tree_counter = 0
line_counter = 0

for position_shift in position_shifts:
    slope_distance = math.ceil((slope_height/position_shift[1]))*position_shift[0]
    slope_multiplier = int(math.ceil(slope_distance/slope_width))

    slope_multiplied = [i*slope_multiplier for i in slope]
    for i in slope_multiplied:
        if position_shift[1] != 1:
            if float(float(line_counter)/float(position_shift[1])).is_integer():
                if i[position[0]] == "#":
                    tree_counter += 1
                position = [position[i] + position_shift[i] for i in range(len(position))]
                line_counter += 1
            else:
                line_counter += 1

        elif position_shift[1] == 1:
            if i[position[0]] == "#":
                tree_counter += 1
            position = [position[i] + position_shift[i] for i in range(len(position))]

    position = [0, 0]

    trees_hit.append(tree_counter)
    tree_counter = 0
    line_counter = 0

result = 1

for i in trees_hit:
    result = result * i

print(trees_hit[1])
print(result)
