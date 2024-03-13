#Loops and list
#Ab, Ebelechukwu Igwagu
#create an empty list
numbers = []
number = int(input("Enter number (0 to quit): "))
#the while statement below checks if number is equal to 0
while number!= 0:
    numbers.append (number)
    number = int(input("Enter another number (0 to quit: "))
# A 'for' and 'in' statement is used to call back d numbers in the list
for value in numbers:
    print (value)
print (numbers)
#to get the float of the average

average = float(sum(numbers))/len (numbers)
print (f"The average is {average}")

