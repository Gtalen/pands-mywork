#A python code based on collatz conjecture
#It prompts the user for a positive integer
#determines if the number is odd or even
#prints off the number sequence using the calculation below
#Author: Ebelechukwu Igwagu

#The line below prompts the  user for a number input
number = int(input("Enter a positive number: "))
numbers = [number]
#ensures that only a positive integer is entered
if number <= 0:
    print ("Please enter a positive integer: ")
#defines the condition statement
while number != 1:
    print (number)
#applies to even numbers
    if  number % 2 == 0:
       number = number/ 2
       #number =("[:.0f] {}"format.number))
#applies to odd numbers
    else:
        number = ((number * 3) + 1)/2
print (1)



# option 2 PENDING COMPLETION
#The line below prompts the  user for a number input
def numbers(number):
    number = int(input("Enter a positive number: "))


#ensures that only a positive integer is entered
while number <= 0:
    print ("Please enter a positive integer: ")
    number = int(input("Enter a positive number: "))
#stores the number in a list
#numbers = [number]

#defines the condition statement
while number != 1:
    print (number)
    if  number % 2 == 0:    #applies to even numbers
       number = number// 2
    else:                   #applies to odd numbers
        number = ((number * 3) + 1)/2
        #numbers.append(number) #appends number to list
        print (numbers)
print (1)


