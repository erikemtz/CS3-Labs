import os
import random

def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2


def process_dir(path):

    dog_list = []
    cat_list = []
    # make arrays to hold filenames and directory names as well as counters
    pics_list = []
    file_list = []
    
    # Your code goes here

    # get current working directory
    temp = path.split('\\')
    tempLength = len(temp)
    currentFolder = temp[tempLength-1]
    print("Currently searching through " + path)
    
    directory_list = []

    file_count = 0
    directory_count = 0

    # get filenames inside directories
    directory_files = os.listdir()

    # classify elements by filetype
    for i in directory_files:
        if os.path.isfile(i):
            if ".jpg" in i:
                file_list.append(os.getcwd() + '\\' + i)
                picture_list.append(os.getcwd() + '\\' + i)
                file_count = file_count + 1
        #if current interation is not a file and not a jpg then it is a directory
        else:
            directory_list.append(i)
            directory_count+=1
            
    pics_list.append(file_list)

    #inform user of what files were found as well as append them to file array

    if file_count == 1 :
        print("There was " + str(file_count) + " picture found...")
        for i in file_list:
            print(os.getcwd() + '\\' + i)
    #this is just so that the print messages are grammatically correct
    elif file_count > 1:
        print("There was " + str(file_count) + " pictures found...")
        for i in file_list:
            print(os.getcwd() + '\\' + i)
    else:
        print("No files pictures found in " + currentFolder)
    
    #pics_list.append(file_list)
    print("")
    print("")

    #then inform user of which directories were found and append them to the directory list
    if directory_count == 1:
        print("There was " + str(directory_count) + " directory found")
        for i in directory_list:
            print(os.getcwd() + '\\' + i)
    #this is just so that the print messages are grammatically correct
    elif directory_count >1:
        print("There was " + str(directory_count) + " directories found")
        for i in directory_list:
            print(os.getcwd() + '\\' + i)
    else:
        print("No directories found in " + currentFolder)    

    print("")
    print("") 

    #if current directory is completely empty,
    if file_count == 0 and directory_count == 0:
        return
    #if current directory has no more directories to traverse through, return files array
    if directory_count == 0:
        return
        
    for i in directory_list:
            #rint(path)
            temp = path+'\\'+i
            os.chdir(temp)
            file_list.append(process_dir(temp))
            os.chdir(path)
    return
    

def main():
    print("***************************************************************************************************************")

    
    process_dir(os.getcwd())

    for i in picture_list:
        if classify_pic(i)>.5:
            dog_list.append(i)
        else:
            cat_list.append(i)
    
    print("Total pictures of dogs found = " + str(len(dog_list)))
    print("Address for dog pictures...")
    print("")
    for i in dog_list:
        print(i)
    
    print("")
    print("")
    print("Total pictures of cats found = " + str(len(cat_list)))
    print("Adress for cat pictures...")
    print("")
    for i in cat_list:
        print(i)


picture_list = []
dog_list = []
cat_list = []

main()


