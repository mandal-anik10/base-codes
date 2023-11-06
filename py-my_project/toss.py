import random
print("please,guess a Head! or Tail! and tap '0' for the toss every time...")
i=1
while i<2:
	a= int(input("..."))
	if a==0:
		b= random.randint(0,1)
		if b==0:
			print("\tHead!")
		else :
			print("\tTail!")
	
	else:
		print("Sorry, can't able to recogonize your command, please tap again...")
