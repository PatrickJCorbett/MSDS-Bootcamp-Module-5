#first just a test, print "hello world"
print("hello world")

##Exercise 1: print the time
#import the datetime function from the datetime package
from datetime import datetime
#put the current time into a variable
now = datetime.now()
#print the current time 
print(now)

##Exercise 2: simple stopwatch

#Create the stopwatch as a function
#import the time package, needed to perform a time delay
import time
def Stopwatch(seconds):
    #Set the Start_Time before waiting 
    Start = datetime.now()
    #wait the number of seconds defined by the seconds argument
    time.sleep(seconds)
    End = datetime.now()
    return(Start, End)
#Run Stopwatch for 10 seconds and store the output in End_Time
Start_Time, End_Time = Stopwatch(10)
print(Start_Time)
print(End_Time)

#Calculate the time elapsed in the stopwatch. Should be equal to the seconds argument used, plus a couple milliseconds
Elapsed = End_Time - Start_Time
print(Elapsed)

##Exercise 3: Print a word provided by the user
def printword():
    word = input("Enter word: ")
    print(word)

printword()

##Exercise 4: Ask for user input and validate that it is a word

#First, will need a dictionary of words to validate against. Can use the nltk library (natural language toolkit)
import nltk
nltk.download('words')
from nltk.corpus import words
#'words' is a corpus, use set to convert to a list. Set converts any iterable (which a corpus is) to a sequence
english_words = set(words.words())

#define function to ask for user input, check if it is in english_words, and return the outcome
def uservalidate():
    #ask user for input
    word = input("Enter input: ")
    #convert to lowercase to match the english_words format
    word_lower = word.lower()
    #if statement: if word_lower is part of the list, say so, otherwise say it isn't
    if word_lower in english_words:
        print("{} is an English word!".format(word))
    else:
        print("{} is not an English word...".format(word))

uservalidate()


##Exercise 5: Print list of user inputs
#function to ask user for num_inputs number of words and then print them all
def userlist(num_inputs):
    #initialize final list of user inputs as a blank list
    userinputs = []
    #for loop for user to input num_inputs number of inputs
    for i in range(0, num_inputs): #this range is used because Python is zero-indexed
        #ask the user to put in word i (I use i + 1 because Python is zero indexed but it sounds better to ask "enter word 1" than "enter word 0")
        word = input("Enter Word {}:".format(i + 1))
        #use the .append method on the userinputs list to add word i
        userinputs.append(word)
    for i in range(0, num_inputs):
        print(userinputs[i])

#Test with three inputs (I used "here" "we" "go")
userlist(3)