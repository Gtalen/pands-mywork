#A python program that opens, reads and counts all the'e's in Mobydick text file
#Author: Ebelechukwu Igwagu

#with open is used to open the file go the variable moby
with open ('mobydick.txt', 'r') as moby:
    mobyDisk = moby.read()  #reads the content of the file
    print (mobyDisk) #prints out the output
    #print (mobyDisk.readline())
eCount = 0
for letter in mobyDisk: #iteration is used to count all the 'e's in the file
   if letter == 'e':
      eCount += 1
print  ("The 'e' count in mobydick is: ", eCount) #outputs the the total count

moby.close() #closes the file

#Referenecs

#Python File Open [WWW Document], n.d. URL https://www.w3schools.com/python/python_file_handling.asp

#Python, R., 2022. Reading and Writing Files in Python (Guide) [WWW Document]. URL https://realpython.com/read-write-files-python/#creating-your-own-context-manager

#Python File Open [WWW Document], n.d. URL https://www.w3schools.com/python/python_file_handling.asp

