# calculation of compound interest

kapital = float(input("Enter your capital "))
zielKapital = float(input("Enter your target capital "))
ZINS = float(input("The interest rate "))
jahr = 0

while kapital<zielKapital:
	kapital = kapital + (kapital * (ZINS/100))
	jahr = jahr + 1

print("It takes %d years" % (jahr))