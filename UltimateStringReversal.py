import random
import sys

menuOptions = ['1','2','3','q']     # menu of actions | 'q' for closing the program
menuMsg = "Select any action by their number...\n1. Letter shuffling(Only for single words).\n2. Word shuffling.\n3. Word's letter shuffling.\nACTION: "

def cleaningString(arg):
    """Cleans the extras of a string"""
    arg = arg.replace("'","")
    arg = arg.replace(",","")
    arg = arg.replace(" ","")
    arg = arg.replace("[","")
    arg = arg.replace("]","")
    return arg

def cleaningList(arg):
    """Cleans the extras of a list of words"""
    arg = arg.replace("'","")
    arg = arg.replace(",","")
    #arg = arg.replace(" ","")
    arg = arg.replace("[","")
    arg = arg.replace("]","")
    return arg

def arrange(var):
    """Arranges the words of a list."""
    words = []
    for i in var:
        word = str(random.sample(i, len(i)))
        word = cleaningString(word)
        words.append(word)
    return words

def run():
    """ controls the program """
    print("\t\t\tString Reversal Program\n\t\t\t   Enter 'q' to exit")
    while True:
        menu = input(menuMsg)

        if menu not in menuOptions:
            print("\t\t\tChoose 1,2 or 3\n")

        elif menu == '1':
            option1 = input("\nInput: ")
            shuffle1 = random.sample(option1, len(option1))
            output1 = cleaningString(str(shuffle1))
            print("Shuffling completed...\n|   "+output1+"   |\n")
        
        elif menu == '2':
            option2 = input("\nInput: ")
            splitted2 = option2.split()                  # splitting the words(else they will all be considered 1 string)
            shuffle2 = random.sample(splitted, len(splitted))
            output2 = cleaningList(str(shuffle2))
            print("Shuffling completed...\n|   "+output2+"   |\n")

        elif menu == '3':
            option3 = input("\nInput: ")
            splitted3 = option3.split()                 # splitting the words(else they will all be considered 1 string)
            arranged3 = arrange(splitted3)
            output3 = cleaningList(str(arranged3))
            print("Shuffing completed...\n|   "+output3+"   |\n")

        elif menu == 'q':
            print("\t\t\tProgram Closed!")
            sys.exit()

run()