"""
A python program that counts all the'e's in the Mobydick text file
Author: Ebelechukwu Chidimma Igwagu
"""
# importing the argument parser as to enable it take a command line argument

import sys

print(sys.argv)





#printsys.argv[1] 
#filename = sys.argv[1]     
#import argparse

# Initialize the ArgumentParser object
#parser = argparse.ArgumentParser()

# Add a positional argument
#parser.add_argument('filepath','filename', help='The filename is "moydick"')

#sys.argv[0]  is the current python file es.py
#sys.argv[1] contains all the other arguments defined in the commandline
#print (f'Name of the script: {sys.argv[0]=}')
#print (f'Arguments of the script : {sys.argv[1:]=}')

#sys.argv[1] is the second argument which is the filename 'mobydick'


if len(sys.argv) != 2:
    print('Usage: python es.py <mobydick>')
    sys.exit(1)

filename = sys.argv[1]      #access filename provided by the user

print (sys.argv[0])
print (sys.argv[1])

# Option 1
try: 
    with open ('mobydick.txt', 'r') as moby:       #with open command is used to open the file to the variable 
        mobydick = moby.read()                     # reads the content of the file
        Count_e = mobydick.count('e')  # counting 'e's
        print  (f"The number of e's in {mobydick} is {Count_e}")

except FileNotFoundError:
    print ('invalid filename: Please enter a valid filename ')

"""
filename = sys.argv[1]      #access filename provided by the user

if len(sys.argv) != 2:
    print('Usage: python es.py <mobydick>')
    sys.exit(1)

# Option 1
try: 
    with open ('filename', 'r') as f:       #with open command is used to open the file to the variable moby
        f_content = f.read()                     # reads the content of the file
        Count_e = f.count('e')  # counting 'e's
        print  (f"The number of e's in {f_content} is {Count_e} ")

except FileNotFoundError:
    print ('invalid filename: Please enter a valid filename ')
# Option 2
 # using iteration to count all the 'e's in the file
"""

"""
e_count = 0
for letter in mobydick: 
   if letter == 'e':
      e_count += 1

print  (f"Mobydick has {e_count} e's")      
"""
moby.close()                                            #closes the file


#try and except

#refernces
#https://www.golinuxcloud.com/python-argparse/
#https://realpython.com/python-command-line-arguments/#the-sysargv-array
