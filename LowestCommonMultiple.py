a = float(input("Enter first number: \n"))
b = float(input("Enter second number: \n"))
cm = 1
cm2 = 1
mul1 = a * cm
mul2 = b * cm2
while (True):
	mul1 = a * cm
	mul2 = b * cm2
	if (mul1 == mul2):
		break
	if (mul1 >= mul2):
		cm2 += 1
	if (mul2 >= mul1):
		cm += 1
	
print(str(a * cm) + " common multiple" )