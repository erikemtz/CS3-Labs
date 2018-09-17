# Course: CS2302
# Author: Rivera, Erik
# Assignments: Lab 1, Option A
# Instructor:Diego Aguirre
# T.A: Manoj Saha
# Last Modification: 9/15/16
# Purpose: Scan jpg images and return the address of pictures of cats and dogs

import os
import random

def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2


def process_dir(path):

    
    # Your code goes here

    # this is used for a future print messages, not being used currently
    # get current working directory
    #temp = path.split('\\')
    #tempLength = len(temp)
    #currentFolder = temp[tempLength-1]
    #print("Currently searching through " + path)
    
    # array used to keep track of directory names
    directory_list = []

    #counters
    file_count = 0
    directory_count = 0

    # get names of all files inside current directory and have them be contained in directory_files
    directory_files = os.listdir()

    # classify elements by filetype and append to appropriate list
    for i in directory_files:
        # if the current file at i is a file and a jpg image, then append to the global variable,  picture_list
        if os.path.isfile(i):
            if ".jpg" in i:
                picture_list.append(os.getcwd() + '\\' + i)
                file_count = file_count + 1
        # if current interation is not a file and not a jpg then it is a directory, append to directory list
        else:
            directory_list.append(i)
            directory_count+=1
            
    
    # UNCOMMENT TO SEE RECURSION IN ACTION
    ###################################################################################################################
    ###################################################################################################################
    # inform user of what files were found as well as append them to file array
    #if file_count == 1 :
        #print("There was " + str(file_count) + " picture found...")
        #dont uncomment print statements, too much info is being displayed, results are the only thing that is needed
        #for i in file_list:
            #print(os.getcwd() + '\\' + i)
    # this is just so that the print messages are grammatically correct
    #elif file_count > 1:
        #print("There was " + str(file_count) + " pictures found...")
        #for i in file_list:
            #print(os.getcwd() + '\\' + i)
    #else:
        #print("No files pictures found in " + currentFolder)
    
    #print("")
    #print("")
    
    # then inform user of which directories were found and append them to the directory list
    #if directory_count == 1:
        #print("There was " + str(directory_count) + " directory found")
        
        #for i in directory_list:
            #print(os.getcwd() + '\\' + i)
    # this is just so that the print messages are grammatically correct
    #elif directory_count >1:
        #print("There was " + str(directory_count) + " directories found")
        #for i in directory_list:
            #print(os.getcwd() + '\\' + i)
    #else:
        #print("No directories found in " + currentFolder)    

    #print("")
    #print("") 
    ###################################################################################################################
    ###################################################################################################################

    # if current directory is completely empty, there is nothing to do, return
    if file_count == 0 and directory_count == 0:
        return
    # if current directory has no more directories to traverse through, return
    if directory_count == 0:
        return
    
    # iterate through all directories recursively within current one
    for i in directory_list:
            temp = path+'\\'+i
            os.chdir(temp)
            process_dir(temp)
            os.chdir(path)
    return
    

def main():
    print("STARTING main.py")
    print("***************************************************************************************************************")

    # lists to contain addresses of dog pictures and cat pictures
    dog_list = []
    cat_list = []

    # find names of all jpg images
    process_dir(os.getcwd())

    # separate the pictures using classify_pic, and populate cat list, and dog list
    for i in picture_list:
        if classify_pic(i)>.5:
            dog_list.append(i)
        else:
            cat_list.append(i)
    
    # print dog results
    print("Total pictures of dogs found = " + str(len(dog_list)))
    print("Address for dog pictures...")
    print("")
    for i in dog_list:
        print(i)
    
    print("")
    print("")
    
    # print cat results
    print("Total pictures of cats found = " + str(len(cat_list)))
    print("Adress for cat pictures...")
    print("")
    for i in cat_list:
        print(i)


# global variable used
picture_list = []

main()
