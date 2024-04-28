"""
A python program that counts all the'e's in a text file
Author: Ebelechukwu Chidimma Igwagu
"""
# importing the argument parser as to enable it take a commandline argument

import sys

# This program makes use of positional argument
#sys.argv[0]  is the first argument and is the python filename es.py
#sys.argv[1] is the second argument argumer which is the users input

filename = sys.argv[1]      #this accesses the filename provided by the user

if len(sys.argv) != 2:
    print('Usage: requires 2 arguments: python <es.py> <filename>')
    sys.exit(1)

print (sys.argv[0])
print (sys.argv[1])

# Option 1
try: 
    with open (filename, 'r') as f:       #opens the text file inputted by the user
        f_content = f.read()                     # reads the text file
        Count_e = f_content.count('e')  # counting all the 'e's in the text file
        print  (f"The number of e's in {filename} is {Count_e}")

except FileNotFoundError:
    print ('invalid filename: Please enter a valid filename ')

f.close()
