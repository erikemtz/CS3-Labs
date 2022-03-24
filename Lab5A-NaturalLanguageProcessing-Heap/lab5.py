from Heap import Heap

def main():
    # create arrays
    heap_array = Heap()
    num_array=[]
    # get all the numbers in num_array
    with open(filename) as file:
        for line in file:
            temp = line.split(",")
            for num in temp:
                num_array.append(num)

    print("Numbers in file are... ")
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