import random
CHOICE_COUNTER = 0

def choose_number():
	global CHOICE_COUNTER
	while True:
		try:
			choice = int(input("Enter Your Guess for this game: "))
			if 1 <= choice <= 100:
				CHOICE_COUNTER += 1
				return choice
			else:
				print("Guess a number between 1 and 100 only")
		except ValueError:
			print("Please enter a valid integer.")

def checker_():
	global CHOICE_COUNTER
	target = random.randint(1, 100)
	choice = choose_number()
	while True:
		if choice == target:
			print("Congratulations! You guessed the correct number.")
			break
		elif choice > target:
			print("Your guess is too high.")
		else:
			print("Your guess is too low.")
		if CHOICE_COUNTER >= 5:
			print("You have Not found the number")
			break
		choice = choose_number()

def main():
	checker_()

main()
	
