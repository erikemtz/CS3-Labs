 # Erik Rivera
# Lab3A
# CS2302 TR @ 10:30-11:50 
# Professor Aguirre, Diego
# TA Saha, Manoj
# Date of last modification 11/5/2018
# Purpose of this lab assigment is to gain familiarity with bst in avl or redblack formats
# This lab uses word embeddings to get the similarity between to words


import string
import random
import math
from AVLTree import AVLTree
from AVLTree import Node
from RedBlackTree import RedBlackTree
from RedBlackTree import RBTNode

# This creates an avl tree from a file based off the glove files
def createAVLTree(file_name):
    print("Creating AVL Tree...")
    avlTree = AVLTree()
    try:

        with open(file_name , encoding = "utf8") as file:
            alphabet = list(string.ascii_letters)
            for line in file:
                array = line.split(" ")
                word = array[0]
                if alphabet.__contains__(word[0]):
                    numbers = []
                    for num in array[1:]:
                        numbers.append(float(num))
                    wordNode = Node(word, numbers)
                    avlTree.insert(wordNode)
    except FileNotFoundError:
        print("File not found...")
        exit()
    return avlTree

# This creates a RedBlack tree from a file based off the glove files
def createRedBlackTree(file_name):
    print("Creating RedBlack Tree....")
    redBlackTree = RedBlackTree()
    with open(file_name, encoding = "utf8") as file:
        alphabet = list(string.ascii_letters)
        for line in file:
            array = line.split(" ")
            word = array[0]
            if alphabet.__contains__(word[0]):
                numbers = []
                for num in array[1:]:
                    numbers.append(float(num))
                wordNode = RBTNode(word, None,None, None, None, numbers)
                redBlackTree.insert_node(wordNode)
    return redBlackTree
    
# This recursively prints a tree in which the ROOT node is given
def __printTree__(root):
    temp = root
    if temp is None:
        return
    __printTree__(temp.left)
    print(temp.key)
    __printTree__(temp.right)


# This method will return a random word in the file
def get_Random_Word(file_name):
    random_int = random.randint(0, get_num_lines(file_name))
    with open(file_name) as file:
        i = 0
        for line in file:
            if i !=random_int:
                i +=1
                continue
            else:
                array = line.split(" ")
                word = array[0]
                alphabet = list(string.ascii_letters)
                if alphabet.__contains__(word[0]):
                    return word
                return get_Random_Word(file_name)
            
# This method will return amount of lines in a file
def get_num_lines(file_name):
    counter = 0
    with open(file_name) as file:
        for line in file:
            counter +=1
    return counter

def ask_user_for_input():
    print("Would you like to use a AVL[1] or Red Black Tree[2]?")
    while True:
            try:
                user_ans = int(input("Please enter 1 or 2...\n"))
            except ValueError:
                print("Sorry that is not a number...\n")
                continue
            if user_ans!=1 and user_ans!=2:
                continue
            else:
                break
    return user_ans

def calculate_similarity_from_file(file_name, user_tree):
    with open(file_name) as file:
        for line in file:
            # Split the words into an array of length 2
            temp_tree = user_tree
            words = line.split(" ")

            first_word = words[0]
            second_word = words[1]
            similarity = 0
            similarity = calculate_similarity_from_pair(first_word, second_word, temp_tree)
            print("Similarity between " + str(first_word) + " and " + str(second_word) + " is " + str(similarity))
    
def calculate_similarity_from_pair(first_word, second_word, user_tree):
    # First look for node in binary tree
    temp = user_tree
    first_word_node = temp.search(first_word)
    second_word_node = user_tree.search(second_word)

    second_word_embedding = second_word_node.get_embedding()
    first_word_embedding = first_word_node.get_embedding()
    
    # Check that both nodes contain embeddings
    if first_word_embedding is not None and second_word_embedding is not None:
        # Variable used for top part of fraction
        top = 0
        # Bottom variables for bottom part of fraction
        bottomA = 0
        bottomB = 0
        embedding_length = len(first_word_embedding)
        for i in range(embedding_length):
            # Top will be the sum of the products
            top = top + (first_word_node.embedding[i] * second_word_node.embedding[i])

            bottomA = bottomA + first_word_node.embedding[i]**2
            bottomB = bottomB + second_word_node.embedding[i]**2
        # Return the similarity
        return (top / (math.sqrt(bottomA) * math.sqrt(bottomB)))

def display_options():
    print("Select an option...")
    print("[1]: Compute the number of nodes in the tree.")
    print("[2]: Compute the height of the tree.")
    print("[3]: Generate file that contains words in the tree.")
    print("[4]: Given depth 'd', generate file with that depth.")
    print("[5]: Exit")

    while True:
        try:
            user_ans = int(input("Please enter 1 trough 5...\n"))
        except TypeError:
            print("Sorry that is not a number...\n")
            continue
        if user_ans<1 and user_ans>4:
            continue
        else:
            break
    
    return user_ans

def compute_amount_nodes(node):
    if node is None:
        return 0
    return 1 + compute_amount_nodes(node.left) + compute_amount_nodes(node.right)

def compute_tree_height(node):
    if node is None:
        return -1
    left_height = compute_tree_height(node.left)
    right_height = compute_tree_height(node.right)
    return max(left_height,right_height)+1
def generate_text_file_from_tree(node, word_file):
    temp = node
    if temp is None:
        return
    generate_text_file_from_tree(temp.left, word_file)
    word_file.write(temp.key + "\n")
    generate_text_file_from_tree(temp.right, word_file)
def generate_text_file_from_tree_depth(node, depth, word_file_depth):
    temp = node
    if depth <0:
        return
    if temp is None:
        return
    generate_text_file_from_tree_depth(temp.left, depth-1, word_file_depth)
    if depth == 0:
        word_file_depth.write(temp.key + "\n")
    generate_text_file_from_tree_depth(temp.right, depth-1, word_file_depth)

def main():

    # Read the file, store each word and its embedding into an avl or redblack tree.
    # Only use words in the text file
    user_ans = ask_user_for_input()
    
    if user_ans == 1:
        print("You chose 1!")
        user_tree = createAVLTree(file_name)
    if user_ans == 2:
        print("Your chose 2!")
        user_tree = createRedBlackTree(file_name)
    # Now we have the tree as user_tree
    
    # Set the variable that holds the word pairs to test
    word_pairs_file_name = "word_pairs.txt"

    # Compare word similarities using pairs file
    calculate_similarity_from_file(word_pairs_file_name, user_tree)

    while True:
        temp = user_tree
        # Display Options
        user_ans = display_options()

        if user_ans == 1:
            amount = compute_amount_nodes(temp.root)
            print("There are " + str(amount) + " nodes")
        if user_ans == 2:
            height = compute_tree_height(temp.root)
            print("The height is " + str(height))
        if user_ans == 3:
            file_name_word = "word_file.txt"
            word_file = open(file_name_word,"w+",encoding =  "utf8")
            generate_text_file_from_tree(temp.root, word_file)
            print("Word file generated: word_file.txt")
        if user_ans == 4:
            file_name_word_depth = "word_file_depth.txt"
            word_file_depth = open(file_name_word_depth, "w+",  encoding =  "utf8")
            while True:
                try:
                    depth = int(input("Enter desired depth.\n"))
                    if depth > compute_tree_height(temp.root):
                        print("Depth too low.")
                        continue
                    else:
                        generate_text_file_from_tree_depth(temp.root, depth, word_file_depth)
                        print("Word file generate: word_file_depth.txt")
                        break
                except ValueError:
                    print("Please enter a number.")
                    continue
                except TypeError:
                    print("Please enter a number.")
                    continue
        if user_ans == 5:
            print("Thank You!")
            exit()

            
file_name = "glove.6b.50d.txt"
main()