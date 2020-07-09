
##Exercise 1: print the current time
#no package outside base r needed: just use the Sys.time() function. With R don't need to wrap in a print statement
Sys.time()


##Exercise 2: simple stopwatch

#Create a stopwatch function
stopwatch <- function(time) {
    #Set the starting time before waiting
    Start = Sys.time()
    #Wait the number of seconds specified by the time arguement
    Sys.sleep(time)
    #Put the time after the end of the stopwatch in a variable
    End <- Sys.time()
    #return this variable
    return(Start, End)
}
#Run the stopwatch, save output to Start_Time, End_Time variables
Start_Time, End_Time <- stopwatch(10)
print(Start_Time)
print(End_Time)
#Calculate the difference. Should be the same as the time argument (give or take some milliseconds)
Elapsed <- End_Time - Start_Time
print(Elapsed)


##Exercise 3: Print a Word Provided by the user

userword <- function() {
    #readline function lets us prompt the user for input, save this to a variable and print
    word = readline(prompt = "Enter word: ")
    print(word)
}

userword()


##Exercise 4:Validate user input

#We will take an english dictionary from the qdapDictionaries package
#documentation of this package: https://cran.r-project.org/web/packages/qdapDictionaries/qdapDictionaries.pdf
#if you don't have it installed:
# install.packages("qdapDictionaries")
#if you do:
library(qdapDictionaries)

#Use GradyAugmented dictionary from this package, which is a vector of 122806 english words
#Define a function to get user input, validate whether it is in GradyAugmented, and an if statement to return the result
uservalidate  <- function(){
    word = readline(prompt = "Enter input: ")
    #force to lower case to conform with GradyAugmented
    word_lower = tolower(word)
    if(word_lower %in% GradyAugmented){
        print(paste0(word," is a word!"))
    }
    else{
        print(paste0(word," is not a word..."))
    }
}

uservalidate()

##Exercise 5: Print list of user input
#Define a function to take num_inputs number of inputs and print them all
userlist  <- function(num_inputs){
    #initialize the final list of inputs as a blank list
    user_inputs = c()
    #for loop to ask user for num_inputs number of inputs and append to the user_inputs list
    for (i in seq(1:num_inputs)){
        word  <- readline(prompt = paste0("Enter word ",i," :"))
        user_inputs  <- c(user_inputs, word)
    }
    #for loop to print out all inputs
    for (i in seq(1:num_inputs)){
        print(user_inputs[i])
    }
}
userlist(3)
