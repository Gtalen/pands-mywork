#program that prompts user to guess a nunmber
#Author: AB, Ebelechukwu Igwagu

number_to_guess = 30
guess = int(input("Guess the number: "))
while guess != number_to_guess:
  if guess < number_to_guess:
    print ("Too low!")
  else:
    print ("Too high!")
#note: That 'guess' needs to start at the same indentation level of if 
#if and else to avoid an infinte loop
    #ctrl + c is used to interrupt an infinte loop
  guess = int(input("Please guess again: "))
print ("Welldone! {} was the number".format (number_to_guess))