bpasses = open("input5.txt","r").read().splitlines()

bids = []
seat_list = []

for bpass in bpasses:
    #Loop to find row
    row_range = [0,127]
    column_range = [0,7]
    for i in range(0,7):
        if bpass[i] == "F":
            row_range = [row_range[0],row_range[1]-((row_range[1]-row_range[0]+1)/2)]
        elif bpass[i] == "B":
            row_range = [row_range[0]+((row_range[1]-row_range[0]+1)/2),row_range[1]]
    #Loop to find column
    for i in range(7,10):
        if bpass[i] == "L":
            column_range = [column_range[0],column_range[1]-((column_range[1]-column_range[0]+1)/2)]
        elif bpass[i] == "R":
            column_range = [column_range[0]+((column_range[1]-column_range[0]+1)/2),column_range[1]]

    bid = row_range[0] * 8 + column_range[0]
    bids.append(bid)
    seat = [row_range[0],column_range[0]]
    seat_list.append(seat)

seat_list = sorted(seat_list)

#Find the missing seat
for i in range(0, len(seat_list)):
    if seat_list[i] == seat_list[0]:
        pass
    elif seat_list[i] == seat_list[-1]:
        pass
    elif (seat_list[i][0] != seat_list[i+1][0]) and (seat_list[i][1] != 7):
        my_seat = [seat_list[i][0],7]
    elif (seat_list[i][0] != seat_list[i+1][0]) and (seat_list[i+1][1] != 0):
        my_seat = [seat_list[i+1][0],0]
    elif (seat_list[i][0] == seat_list[i+1][0]) and (seat_list[i+1][1] != (seat_list[i][1]+1)):
        my_seat = [seat_list[i][0],seat_list[i][1]+1]
    else:
        pass

my_seat_id = my_seat[0] * 8 + my_seat[1]

print(max(bids))
print(my_seat_id)
