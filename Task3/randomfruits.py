#A progra that prints off random fruits from a tuple
#Author: Ebelechukwu Igwagu
import random
fruits = ['apples, kiwi, banana, pineapple, orange, tangerine']

#To prints a random number between the legth of fruits
#the eindex 0 and -1 is used. where 0 i sthe first indices and -1 the last

index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print("A random fruit: {}".format(fruit))

mkpuruosisi = ['apples, kiwi, banana, pineapple, orange, tangerine']
index = random.randint(0,len(mkpuruosisi)-1)
osisi =mkpuruosisi[index]
print ("A Arandom osisi: {}".format(mkpuruosisi))

message = 'I have eaten ' + str (99) + ' burritos'
print (message)