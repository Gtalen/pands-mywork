#random numbers in a queue
queue  = []
import random
numberofNumbers = 10
rangeTo = 100
for i in range(0, numberofNumbers):
    queue.append(random.randint(0,rangeTo))

print (f"queue is {queue}")  

while len(queue) != 0:
    currentNumber = queue.pop(0)
    #print ("current number is {} and the queue is {}".format(currentNumber, queue))
    print (f"current number is {currentNumber} and the queue is {queue}")
print ("The queue is now empty")

