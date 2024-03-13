#This programme reads in a students percentage
#it prints off the corresponding grade
#Author: Ab, Ebelechukwu Okafor
percentage = float(input("Enter the percentage: "))
print ("{}%".format(percentage))
#rounding the score to the nearest whole number
print ("{:.0f}%".format(percentage))
#and/or will be used to define the grade to print off
if percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100")
elif percentage < 40:
    print ("Fail")
elif percentage < 50:
    print ("Pass")
elif percentage < 60:
    print ("Merit1")
elif percentage < 70:
    print ("Merit2")
else:
    print ("Distinction")
