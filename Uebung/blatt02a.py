# Leap year calculator

print("Enter the year of interest:")
jahr = int(input())

if jahr % 4 == 0:
	if jahr % 100 == 0:
		if jahr % 400 == 0:
			print(str(jahr) + " is a leap year")
		else:
			print(str(jahr) + " is not a leap year")
	else:
		print(str(jahr) + " is a leap year")
else:
	print(str(jahr) + " is not a leap year")	

