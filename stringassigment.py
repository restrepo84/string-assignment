#!/usr/bin/python3

def main():
    #get string input from the user
    phrase = input("Type in a word or phrase: ")

    #print out each letter separately
    print("These are the letters in your input")
    for c in phrase:
        print(c)

    #print out the letters in reverse order
    print("")
    print("These are the letters in your input in reverse order")
    counter = len(phrase) - 1
    while counter >= 0 :
        print(phrase[counter])
        counter -= 1

    #get letter from user
    letter = input("Enter a letter: ")
    counter = 0

    #count times letter appears in word/phrase
    for c in phrase:
        if letter.lower() == c.lower():
            counter += 1

    #output times letter appeared
    if counter == 1:
        print("The {} appeared 1 time in '{}'".format(letter, phrase))
    else:
        print("The {} appeared {} times in '{}'".format(letter, counter, phrase))
        
if __name__ == "__main__": main()
