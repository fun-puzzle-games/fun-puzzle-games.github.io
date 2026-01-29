import random 

print("Welcome to the Number Guessing Game! \nYou have 5 chances to guess the number")
computer_guess=random.randint(1,10)
chances=5
counter=0 #THe conter variable is used to keep track of the chances in the game
# THe flag variable is used to signal wether a specific condition has been met. It essentially acts as a marker to control the flow and logic of the program.
success=False

#print("The correct number was: ", computer_guess)



while counter < chances:
    counter = counter + 1
    guess=int(input("Enter a number between 1 and 10: ")) 
    
    if guess == computer_guess:
        print(f'Correct! The number is {computer_guess}. You guessed it in {counter} tries!')
        success=True
        break
    else:
        print("Wrong guess. Try again!")
if not success:
      print(f'Sorry! The number was {computer_guess}. Better luck next time!')
 
