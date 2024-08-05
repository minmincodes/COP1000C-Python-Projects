#
#   Minh D Le
#
#   bigGame.py
#
#   A MadLib Game that creates a story with user inputs
#

def main():

    #   prints name of game and instructions

    print("MADLIB GAME")
    #   empty print() creates space between strings when executed
    print()

    print("Enter the following words: ")
    #   prompts user for inputs
    
    pNoun1 = input("A Plural Noun: ")
    
    fName = input("First Name: ")
    
    noun1 = input("Noun: ")
    
    lName = input("Last Name ")
    
    pNoun2 = input("Plural Noun: ")
    
    place1 = input("Place: ")
    
    pNoun3 = input("Plural Noun: ")
    
    place2 = input("Place: ")
    
    pNoun4 = input("Plural Noun: ")
    
    noun2 = input("Noun: ")
    
    adj1 = input("Adjective: ")
    
    adj2 = input("Adjective: ")
    
    verb = input("Verb: ")
    
    adj3 = input("Adjective: ")

    #   print game intro

    print()

    print("The Big Game!!!")
    
    #   print madlib game using user inputs

    print()
    
    print("Hello there, sports",pNoun1,"!")
    print("This is",fName, ", talking to you from the press",noun1,)
    print("in",lName,"Stadium, where 57,000 cheering",pNoun2,)
    print("have gathered to watch (the)",place1,pNoun3,)
    print("take on (the)",place2,pNoun4,".")
    print("Even though the",noun2,"is shining, it's a/an",adj1,)
    print("cold day with the temperature in the",adj2,"20s.")
    print("We'll be back for the opening",verb,"-off after a few words")
    print("from our",adj3,"sponsor.")
    

main()
