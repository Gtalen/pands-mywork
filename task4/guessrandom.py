#A program that generates a random number 
#prompts user to guess the number
#Author: Ebelechukwu Igwagu
#import random module

import random
number = random.randint(0,100)
print (number)
guessrandom = int(input("Guess the random number: "))
while guessrandom != number:
   if guessrandom < number:
     print ("Too low!")
   else:
     print ("Too high!")
   guessrandom = int(input("Please try again: "))
guessrandom == number
print ('Terrific! You are a genius. Number is {}'.format(number))