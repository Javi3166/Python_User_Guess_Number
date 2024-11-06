import random

#Ranges for the random variable
minimum_range = 1
maximum_range = 100

#Generates a number between 1 and 10
number_to_guess = random.randint(minimum_range, maximum_range)

guess_successful = False
user_guess = 0

print("Please guess a number between " + str(minimum_range) + " and " + str(maximum_range) + ".")

#The "not" in this case is always equivalent to "== False".
while not guess_successful:
    #User input is always a string so needed to convert it to an int in order to be able to compare.
    user_guess = int(input("Please input a guess: "))
    if user_guess == number_to_guess:
        print("Success! You guessed it correctly!")
        guess_successful = True
    elif user_guess > number_to_guess:
        print("Please guess again. It was too high.")
    elif user_guess < number_to_guess:
        print("Please guess again. It was too low.")