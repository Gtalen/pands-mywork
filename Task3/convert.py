#dollar to cent conersion
#Author: Ebelechukwu Igwagu
amount = float (input("Enter the amount: "))
dollaramount = print ("${:.2f}".format(amount))
#formats dollar amount to 2 decimal places
floated = (float(amount * 100))
#{:.0f} displays the number in 0 decimal places
amount_in_cent = ("{:.0f}").format(floated)
print (amount_in_cent)
print (str(amount_in_cent) + 'cent')
#format is used to concatenate strings and integer without conversion
print ("{} cent'".format(amount_in_cent))