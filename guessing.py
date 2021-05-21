import random
number=random.randint(1, 9)
chances=0
while chances < 3:
	guess=int(input("enter the number"))
	if guess==number:
		print ("YOU GUESSED IT RIGHT, CONGRATULATIONS")
		break
	elif guess < number:
		print ("please guess a higher number")
	else:
		print ("please guess a lower number")
	chances=chances+1
if not chances < 3:
	print ("u lost the game :(", number)

