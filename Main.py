import os
import random


def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]

    return dir_list, file_list


def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        print("Found Dog Pic")
        return 0.5 + random.random() / 2

    print("Found Cat Pic")
    return random.random() / 2


def process_dir(path):

    dir_list, file_list = get_dirs_and_files(path)

    cat_list = []
    dog_list = []

    # Your code goes here
    if path=="":
        print("End...")
        return
    os.walk(path)
    for i,j,k in os.walk(path):
        print(i)
        classify_pic(i)
    


def main():
    start_path = './' # current directory

    process_dir(start_path)


main()
