import math

list_of_ids = []
file = open('input.txt', 'r')
for line in file:
	front = 0
	back = 127
	left = 0
	right = 7
	finalrow = 0
	finalcolumn = 0
	for i, letter in enumerate(line):
		if letter == 'F':
			back = math.floor((front + back)/2)
			finalrow = front
		if letter == 'B':
			front = math.ceil((front+back)/2)
			finalrow = back
		if letter == 'R':
			left = math.ceil((left+right)/2)
			finalcolumn = right
		if letter == 'L':
			right = math.floor((left+right)/2)
			finalcolumn = left
	list_of_ids.append(finalrow * 8 + finalcolumn)

list_of_ids.sort()
for i in list_of_ids:
	if i + 1 not in list_of_ids:
		print(i+1)
		break