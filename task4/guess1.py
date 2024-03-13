#program that prompts user to guess a nunmber
#Author: AB, Ebelechukwu Igwagu

number_to_guess = 30
guess = int(input("Guess the number: "))
while guess != number_to_guess:
    print ("Wrong")
    guess = int(input("Please guess again: "))
print ("Welldone! {} was the number".format (number_to_guess))