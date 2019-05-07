# Christmas tree

hoehe = int(input("Enter the height of the Christmas tree: "))

for i in range(1,hoehe):
	y = i*2
	x = hoehe - i
	for j in range(1,x):
		print(" ", end = '')
	for n in range(1,y):
		print("*", end = '')
	print()