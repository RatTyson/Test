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

fruits = "apple", "banana", "carrot"
a, b, c = fruits

print("welcome to this place\n")

name = input("What is your name\n")
age = int(input("how old are you\n"))

if age >= 18:
	print("please continue to the next step\n")
else:
	print("You aren't old enough to enter\n")

print("hey", name, 'welcome to my practice\n')

print("you will be " + str(age + 10 ) , 'in 10 years')

print("you have", str(len(name)) , 'letters in your name')

fruits = input("what does your favorite fruit start with\n")
if fruits == (a,b,c):
	print(fruits)
