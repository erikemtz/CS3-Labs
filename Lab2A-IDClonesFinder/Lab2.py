# Erik Rivera
# 10/11/2018

import os.path
from os import path
import random
import time


class Node():
    def __init__(self, d=None , n=None):
        self.data= d
        self.n = None

class LinkedList():
    def __init__(self, root=None):
        self.root = Node()
        self.size = 0
    def get_size(self):
        return self.size
    def add(self, d):
        if self.size is 0:
            self.root = Node(d)
            self.size += 1
            return
        newNode = Node(d)
        temp = self.root
        while temp.n is not None:
            temp = temp.n
        temp.n = newNode
        self.size+=1
    def addNode(self, node):
        if self.size is 0:
            self.root = node
            self.size +=1
            return
        temp = self.root
        while temp.n is not None:
            temp = temp.n
        temp.n = node
        self.size+=1
    def find(self, position):
        if position > self.size:
            print ("Index out of range...")
        else:
            temp = self.root
            tempInt = 1
            while(tempInt<position):
                temp = temp.n
                tempInt += 1
        return temp.data

    def printList(self):
        temp = self.root
        while(temp is not None):
            print(temp.data)
            temp = temp.n
    def getMiddle(self):
        return self.size/2

    def bubbleSort(self):
        tempNode = self.root
        nextTempNode = tempNode.n
        while(tempNode.n is not None):
            while(nextTempNode is not None):
                if tempNode.data > nextTempNode.data:
                    tempInt = tempNode.data
                    tempNode.data = nextTempNode.data
                    nextTempNode.data = tempInt
                nextTempNode = nextTempNode.n
            tempNode = tempNode.n
            nextTempNode = tempNode.n

#END CLASSES
##############################################################################################################################
def mergeSort(list1):
    if len(list1)<=1:
        return list1
    midPoint = int(len(list1)/2)
    left, right = mergeSort(list1[:midPoint]), mergeSort(list1[midPoint:])
    return mergeList(left, right)

def mergeList(left, right):
    result = []
    leftInt = rightInt = 0
    while leftInt < len(left) and rightInt<len(right):
        if left[leftInt] < right[rightInt]:
            result.append(left[leftInt])
            leftInt +=1
        else:
            result.append(right[rightInt])
            rightInt+=1
    result.extend(left[leftInt:])
    result.extend(right[rightInt:])
    return result

def linkedListToArray(tempList):
    tempNode = tempList.root
    tempArray = []
    while tempNode is not None:
        tempArray.append(tempNode.data)
        tempNode = tempNode.n
    return tempArray

def solution1(list1):
    cloneArray = []
    array1 = linkedListToArray(list1)
    for i in range(len(array1)):
        for j in range(len(array1)):
            if j <= i:
                continue
            elif array1[i] == array1[j]:
                if array1[i] not in cloneArray:
                    cloneArray.append(array1[i])
                    #print("Found clone: " + str(array1[i]))
    print("Clone list size: " + str(len(cloneArray)))
                

def solution2(list1):
    cloneArray = []
    print("Sorting list...")
    list1.bubbleSort()
    print("Iterating...")
    temp = list1.root
    while temp.n is not None:
        if temp.data == temp.n.data:
            if temp.data not in cloneArray:
                    cloneArray.append(temp.data)
                    #print("Found clone id's: " + str(temp.data))
        temp = temp.n
    print("Clone list size: " + str(len(cloneArray)))

def solution3(list1):
    cloneArray = []
    tempArray = linkedListToArray(list1)
    print("Sorting...")
    mergeSort(tempArray)
    for i in range(len(tempArray)-1):
        if tempArray[i] == tempArray[i+1]:
            if tempArray[i] not in cloneArray:
                cloneArray.append(tempArray[i])
                #print("Found clone id's: " + str(tempArray[i]))
    print("Clone list size: " + str(len(cloneArray)))

def solution4(list1): 
    tempArray = linkedListToArray(list1)
    cloneArray = []
    seen = [None]*(max(tempArray)+1)
    for i in range(len(tempArray)):
        if seen[tempArray[i]] == True:
            if tempArray[i] not in cloneArray:
                #print("Found clone: " + str(tempArray[i]))
                cloneArray.append(tempArray[i])
        else:
            seen[tempArray[i]] = True
    print("Clone list size: " + str(len(cloneArray)))

#END METHODS########
def main():
    print("STARTING MAIN...")
    # Optional choice to ask the user to enter the file names that contain txt data
    '''
    print("Enter file name for first txt file, (dont include .txt)")
    
    # Scan first file input
    while True:
        firstFile = input("")
        firstFileAsTxt = firstFile+".txt"
        if(path.exists(firstFileAsTxt)):
            print("File Found! : " + firstFileAsTxt)
            break
        else:
            print("File not found, make sure it in the same directory as this program...")

    # Scan second file input

    print("Enter file name for second txt file, (dont include .txt)")
    while True:
        secondFile = input("")
        secondFileAsTxt = secondFile+".txt"
        if(path.exists(secondFileAsTxt)):
            print("File Found! : " + secondFileAsTxt)
            break
        else:
            print("File not found, make sure it in the same directory as this program...")

    # For testing purposes
    
    print("Generating random text files...")
    # Create test files filled with random integers, numbers will range from 0 to 50
    file = open("randomInts10.txt", "w+")
    for i in range(10):
        file.write(str(random.randint(0,51)) + '\n')

    file = open("randomInts100.txt", "w+")
    for i in range(100):
        file.write(str(random.randint(0,51)) + '\n')

    file = open("randomInts1000.txt", "w+")
    for i in range(1000):
        file.write(str(random.randint(0,51)) + '\n')

    file = open("randomInts10000.txt", "w+")
    for i in range(10000):
        file.write(str(random.randint(0,51)) + '\n')
    
    # Create test linked lists that consist of random integers from txt files generated previosly
    listSize10 = LinkedList()
    with open("randomInts10.txt") as file:
        for line in file:
            listSize10.add(int(line))
    listSize100 = LinkedList()
    with open("randomInts100.txt") as file:
        for line in file:
            listSize100.add(int(line))
    listSize1000 = LinkedList()
    with open("randomInts1000.txt") as file:
        for line in file:
            listSize1000.add(int(line))
    listSize10000 = LinkedList()
    with open("randomInts10000.txt") as file:
        for line in file:
            listSize10000.add(int(line))

    millis = int(round(time.time()))
    print("Time: " + str(millis))
    '''

    #### START ####

    mainList = LinkedList()

    firstFileName = "vivendi.txt"
    secondFileName = "activision.txt"

    # Iterate through both files, add elements to mainList
    with open(firstFileName) as file:
        for line in file:
            mainList.add(int(line))
    with open(secondFileName) as file:
        for line in file:
            mainList.add(int(line))
    
    ## SEARCH FOR CLONES USING THE 4 SOLUTIONS ##

    # Solve for clones using solution 1 (nested loops)
    print("")
    print("Using solution 1 (Nested Loops)...")
    currTime = time.time()
    solution1(mainList)
    elapsedTime = time.time() - currTime
    print("Elapsed time: " + str(elapsedTime))

    # Solve for clones using solution 2 (neighbors) using bubblesort
    print("")
    print("Using solution 2 (Bubblesort)...")
    currTime = time.time()
    solution2(mainList)
    elapsedTime = time.time() - currTime
    print("Elapsed time: " + str(elapsedTime))

    # Solve for clones using solution 3 (neighbors) using mergesort
    print("")
    print("Using solution 3 (MergeSort)...")
    currTime = time.time()
    solution3(mainList)
    elapsedTime = time.time() - currTime
    print("Elapsed time: " + str(elapsedTime))

    # Solve for clones using boolean array
    print("")
    print("Using solution 4 (Hashmap)...")
    currTime = time.time()
    solution4(mainList)
    elapsedTime = time.time() - currTime
    print("Elapsed time: " + str(elapsedTime))
main()