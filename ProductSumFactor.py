sum = float(input("Enter a number: \n"))
pro = float(input("Enter a Product: \n"))

c1 = 1
if (pro < 0):
	c1 = -1
while ((c1 != pro) and (pro != 0)):
	
	if (sum == 1):
			c1= 1
			c2 = 1
			print(str(1) + " and " + str(1) + " are factors 56666ģ")
			break
	elif (pro > 0 and sum > 0):
		c1 += 1
		c2 = sum - 1
		while (c2 > 0):
			if ((pro % c1 == 0) and (pro % c2 == 0)):
				print(str(c1) + " and " + str(c2) )
				if (c1 + c2 == sum and c1 * c2 == pro):
					print(str(c1) + " and " + str(c2) + " are factors 56666ģ")
					pro = 0
					break
				
			c2 -= 1
			
	elif (pro < 0 or sum > 0):
		c1 -= 1
		c2 = 2
		while (c2 < -pro):
			if ((pro % c1 == 0) and (pro % c2 == 0)):
				print(str(c1) + " and " + str(c2) )
				if (c1 + c2 == sum and c1 * c2 == pro ):
					print(str(c1) + " and " + str(c2) + " are factors 2")
					pro = 0
					break
				
			c2 += 1
	else:
		print("nooòoooo")
		break
	
			
print(str(c1) + " and " + str(c2) + " are factors final")