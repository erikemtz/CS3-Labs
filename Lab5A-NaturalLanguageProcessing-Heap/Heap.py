# Erik Rivera
# CS2302 TR 10:30 - 11:50
# Aguirre Diego
# 11/29/2018

class Heap:
    def __init__(self):
        self.heap_array = []
    
    def insert(self, k):
        print("Inserting " + str(k))
        # first insert the element in the array
        self.heap_array.append(k)
        # then sort the list/heap
        self.sort()

    # remove the first 
    def extract_min(self):
        if self.is_empty():
            print("List is empty")
            return None
        # save the min element in the array
        min_elem = self.heap_array[0]
        # set the last element as the root element
        self.heap_array[0] = self.heap_array[len(self.heap_array)-1]
        # get rid of the last element so it is not repeated
        self.heap_array.pop()
        # resort the list
        self.sort()
        # return min
        return min_elem

    # Returns true if the length is 0, else its false
    def is_empty(self):
        return len(self.heap_array)==0

    def sort(self):
        # create boolean variable
        sorted = False
        while not sorted:
            swapped = False
            # iterate through array until no swaps are needed
            for i in range(1, len(self.heap_array)):
                # if the current element is less that its parent, then swap
                if self.heap_array[i] < self.heap_array[(i-1)//2]:
                    temp = self.heap_array[(i-1)//2]
                    self.heap_array[(i-1)//2] = self.heap_array[i]
                    self.heap_array[i] = temp
                    swapped = True
            # if no swaps were needed then the array is sorted
            if not swapped:
                sorted = True
    def print(self):
        for num in self.heap_array:
            print(num)
