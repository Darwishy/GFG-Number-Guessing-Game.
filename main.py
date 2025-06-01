#intro / how many guesses they get.
#Ask the user a range of numbers they want to guess.
#Pick a random number between the users range
#Ask the user for a number between the range they inserted.
#check if number == to the number or if its higher or lower.
#return if its too high or too low or correct.
import random

user_Name = input("Hey, what is your name ?: ")
print(f"Hello {user_Name} and welcome to the Number Guessing Game. You get 7 Tries to guess.")
print("I need you to give a range of numbers you want to guess between")
number_One = int(input("First the lowest number: "))
number_Two = int(input("And the highest number: "))
random_Num = random.randint(number_One, number_Two)

guesses = 7 #could let the user choose by making it a input.

while guesses > 0:
    user_guess = int(input("Guess a number: "))
    if user_guess == random_Num:
        print(f"WOW, You got it ! it was indeed {random_Num}")
        break
    elif user_guess < random_Num:
        print(f"{user_guess} is too low, {guesses -1}/7 tries left")
        guesses -= 1
    else:
        print(f"{user_guess} is too high, {guesses -1}/7 tries left")
        guesses -= 1

    if guesses == 0:
        print("You ran out of tries. Good luck next time !")
        break