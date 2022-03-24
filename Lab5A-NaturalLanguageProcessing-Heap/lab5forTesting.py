from Heap import Heap
from random import randint
def main():
    
    # create arrays
    heap_array = Heap()
    num_array=[]

    # THIS WILL GENERATE RANDOM NUMBERS AND APPEND THEM
    while True:
        try:
            amount = int(input("Enter amount of random numbers..."))
            break
        except ValueError:
            print("Enter valid integer number...")
    for num in range(amount):
        num_array.append(randint(0,999999))


    # THIS WILL TAKE USER INPUT UNTIL -1 IS ENTERED
    # while True:
    #     try:
    #         number = int(input("Enter number..."))
    #         if number == -1:
    #             break
    #         num_array.append(number)
    #     except ValueError:
    #         print("Value Error...")
    

    # THIS WILL READ THE FILE
    # with open(filename) as file:
    #     for line in file:
    #         temp = line.split(",")
    #         for num in temp:
    #             num_array.append(num)

    print("Numbers in array are... ")
    for num in num_array:
        print(num)
    # insert into heap
    print("Using heap sort...")
    for num in num_array:
        heap_array.insert(num)

    print("Numbers are ...")
    while not heap_array.is_empty():
        print(heap_array.extract_min())

    
filename = "numbers.txt"
main()