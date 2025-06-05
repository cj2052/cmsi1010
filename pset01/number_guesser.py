
import random

def NumberGuesser():
    print("")
    print("To pass Number Guesser, you must guess the number that the Mystical Monty has chosen for you. Guess a number between 1 and 1000.")
    print("Please type 'Bye' or 'Exit' to quit the program.")
    print("")
    #Intro strings when program is initiated or restarted

    random_number = random.randint(1,1001) 
    #creates random number between 1 and 1000
    guess_attempts = 0 
    #creates guess attempts variable and zeroes it out at the beginning of the program

    GuessMonty(random_number, guess_attempts) 
    #calls the guessing game function with parameters so that there is a new random number each game and attempts are zeroed

def GuessMonty(random_number, guess_attempts):
    while True:
        response = input("Please type your guess for the number that Monty has chosen:").strip().lower() 
        #takes input from the user
        try:
            response_int = int(response) 
            #turns the input from a string into an integer so it can be compared to Monty's random number
            if response_int not in range(1,1001): 
                print("Please enter a valid number.") 
                #ensures that the number guessed is within the range
            elif response_int < random_number:
                print("Too Low!") 
                #compares the number guessed to Monty's number and tells if it's too low
                guess_attempts = guess_attempts + 1
            elif response_int > random_number:
                print("Too High!")
                #compares the number guessed to Monty's number and tells if it's too high
                guess_attempts = guess_attempts + 1
            elif response_int == random_number:
                print("Congratulations! You guessed the number!", "Attempts:", (guess_attempts + 1)) #tells the user that their guess is correct and tells how many guesses they took
                NumberGuesser() 
                #restarts the NumberGuesser() function which creates a new random number, zeroes the attempts count, and restarts the GuessMonty() function
            else:
                print("Please enter a valid number") 
                #this should never be reached, it's just there as a 'just in case'
        except ValueError: 
            #this ensures that there isn't an error message when a string (or something else) is input by the user
            if response == "bye": 
                print("The Mystical Monty will see you next time!") 
                #I tried to use "if response == 'bye' or 'exit':" but for some reason that always came back as true no matter what I typed
                # so I separated them into two if statements
                break 
                # ends the program 
            elif response == "exit":
                print("The Mystical Monty will see you next time!")
                break 
                #There is a bug where when I play multiple times typing 'exit' doesn't get me out of the program, it just prints the message
                # ... but typing 'bye' works just fine
                #Typing 'exit' works on the first play through, though
                #I'm not sure why this is...... they both should do exactly the same thing???
            else:
                print("Please enter a valid number")
                continue
                # again this should never actually be reached it's just a 'just in case'

NumberGuesser()
#this starts the program the first time