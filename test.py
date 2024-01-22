#this is used everytime you level up
def level_up():
	print("You just leveled up!\n")
	reward = input('Would you like a sword or a shield?')
	if reward == "shield":
		print("you've gained a new shield")
		if reward == "sword":
			print("you gained a shield")
	else :
		print("please choose a reward")


print("welcome to this place\n")

name = input("What is your name\n")
age = input("how old are you\n")

print("hey", name, 'ie\n')

level_up()
