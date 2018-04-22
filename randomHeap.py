from random import randrange
from pythonds.trees import binheap

# Method will generate random ints between 0 and 100
def createList(length):
    randomList = []
    i = 0
    for i in range(0,length):
        randomInt = randrange(1,100)
        randomList.append(randomInt)
        i += 1
    return randomList

# Takes in a list and uses it to make a heap
def newHeap(myList):
    myHeap = binheap.BinHeap()
    myHeap.insert(myList)
    myHeap.buildHeap(myList)
    return newHeap
    
def main():
    length = int(input('How long is your list?'))
    aList = createList(length)
    print('Your random list: ', aList)
    print('Resulting heap tree:')
    print(newHeap(aList))

main()