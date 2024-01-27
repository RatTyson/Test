#this is used everytime you level up
def level_up():
	print("You just leveled up!\n")
	while True:
		reward = input('Would you like a sword or a shield? ')
		if reward == "shield":
			print("you've gained a new shield")
			break
		elif reward == "sword":
			print("you gained a sword")
			break
		#need a way to repeat command if they dont choose either or
		elif reward != "shield" or "sword":
			print("please choose a reward ")
	
level_up()
fruits = "apple", "banana", "carrot"
a, b, c = fruits

print("welcome to this place\n")

#asks for name and age
while True:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))  # Assuming you're getting the age from user input

    if len(name) >= 10:
        print("You're only allowed to have 10 characters in your name.")
    elif age < 18:
        print("You aren't old enough to enter.")
    else:
        input("Please continue to the next step.\n")
        break  # Exit the loop if both conditions are met
else:
    print("Unexpected error occurred.")  # This will be printed if the loop exits unexpectedly

password = input("please make a password ")

print("hey", name, 'welcome to my practice\n')
input()

print("you will be " + str(age + 10 ) , 'in 10 years')

print("you have", str(len(name)) , 'letters in your name')
input()
fruits = input("what does your favorite fruit start with\n")
if fruits == (a,b,c):
	print(fruits)


while True:
    userInput = input("Please enter your password: ")
    if userInput == password:
        print("You may continue.")
        break
    else:
        print("Incorrect password.")
