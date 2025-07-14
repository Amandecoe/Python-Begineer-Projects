MAX_LINES = 3
MAX_BET = 100   #This are constants which can be used anywhere in the program.
MIN_BET=1



def deposit(): # Function to deposit money into an account
   while True: #  loop to ensure a valid amount is entered
      amount = input ("How much would you like to deposit? $")
      if amount.isdigit(): #checks if the input is a whole number
         amount = int(amount) # converts the input to an integer if what they entered is a valid whole number
         if amount > 0: #then if the entered and converted amount is greater than 0 it displays the else statements
            break
         else:
            print("Amount must be greater than 0.") #Displays this if amount is < 0
      else: 
         print ("Please enter a number") #Displays this if they enter a different value than a digit
   return amount

def get_bet():
   while True: #  loop to ensure a valid amount is entered
      amount = input ("What would you like to bet on each line? $")
      if amount.isdigit(): #checks if the input is a whole number
         amount = int(amount) # converts the input to an integer if what they entered is a valid whole number
         if MIN_BET <= amount <= MAX_BET: #then if the entered and converted amount is greater than 0 it displays the else statements
            break
         else:
            print(f"Amount must be between ${MIN_BET} - ${MAX_BET}") #Displays this if amount is not between max and min bet
      else: 
         print ("Please enter a number") #Displays this if they enter a different value than a digit
   return amount



def get_number_of_lines():
    while True: #  loop to ensure a valid amount is entered
      Lines = input ("Enter the number of lines to bet on (1 -" + str(MAX_LINES) + ")? ")
      if Lines.isdigit(): #checks if the input is a whole number
         Lines = int(Lines) # converts the input to an integer if what they entered is a valid whole number
         if 1 <= Lines <= MAX_LINES: #then if the entered and converted amount is greater than 0 it displays the else statements
            break
         else:
            print("Please enter a valid number of lines") #Displays this if amount is not a valid number of lines
      else: 
         print ("Please enter a number") #Displays this if they enter a different value than a digit

    return Lines



def main():
 balance = deposit()  
 lines = get_number_of_lines()
 while True:   #check if user enters a valid balance also chooses valid number of lines then proceed
    bet = get_bet()
    total_bet = bet * lines

    if total_bet > balance:
        print(f"You do not have enough to bet that amount, your current balance is {balance}")
    else: 
        break

print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
 
main()
