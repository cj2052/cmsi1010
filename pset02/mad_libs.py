import random 

templates = [
    {
        "text": " The :adjective life is not worth :ing_verb", 
        "author":"Socrates"
}, 
    {
        "text": "The life of man (in a state of nature) is :adjective , :adjective , :adjective , :adjective , and :adjective", 
        "author":"Thomas Hobbes"
}, 
    {
        "text": "I :verb therefore I :verb", 
        "author": "Descartes", 
    }, 
    {
        "text": "One cannot :verb twice in the same :noun", 
        "author": "Heraclitus", 
    }, 
    {
        "text": "The mind is not a :noun to be :past_verb , but a :noun to be :past_verb", 
        "author": "Plutarch", 
    }, 
    { 
        "text": "The journey of a :number :noun begins with a single :noun .", 
        "author": "Lao Tzu", 
    }, 
    {
        "text": "That which does not :verb us makes us :adjective_comparative", 
        "author": "Nietzche", 
    }, 
    {
        "text": ":noun is power", 
        "author": "Sir Francis Bacon", 
    }, 
    {
        "text": "Man is born :adjective , and everywhere he is in :noun", 
        "author": "Jean-Jacques Rousseau", 
    }, 
    {
        "text": "We have two :body_part and one :body_part , so we should :verb more than we :verb", 
        "author": "Zeno of Citium", 
    }
]

def check_input(prompt):
    # This function receives an input from the user and checks it to make sure that it is a reasonable length.
    # It then return the user response to pass into the mad_libs_sentence function.
    # This function runs a recursion to continue evaluating the input if it is invalid the first time, only returning
    # the response when it falls within a valid length parameter.
    response = input(prompt).strip().lower()
    if len(response) < 1 or len(response) > 30:
        print("Please enter a valid response")
        return check_input(prompt)
    else:
        return response
    

def replace_words(word):
    # This function takes the response from check_input and replaces the word in the template with the new word from the user.
    # It returns the new word to be joined in mad_libs_sentence with the rest of the sentence. 
    if word == ":adjective":
        new_word = word.replace(word, check_input("Please input an adjective:"))
    elif word == ":ing_verb":
        new_word = word.replace(word, check_input("Please input a verb that ends with -ing:"))
    elif word == ":number":
        new_word = word.replace(word, check_input("Please input a number:"))
    elif word == ":verb":
        new_word = word.replace(word, check_input("Please input a verb:"))
    elif word == ":noun":
        new_word = word.replace(word, check_input("Please input a noun:"))
    elif word == ":past_verb":
        new_word = word.replace(word, check_input("Please input an verb in the past tense:"))
    elif word == ":adjective_comparative":
        new_word = word.replace(word, check_input("Please input a comparative adjective (e.g. better, grander, bigger):"))
    elif word == ":body_part":
        new_word = word.replace(word, check_input("Please input a body part:"))
    else:
        # this is just for debugging purposes
        raise ValueError("Something is wrong")
    return new_word
  

def mad_libs_sentence():
    sentence_pieces = []
    current_template = random.choice(templates)
    # This checks if the word in the template has a : in front (to mark that it needs to be replaced)
    for word in current_template["text"].split():
        if word.startswith(":"):
            sentence_pieces.append(replace_words(word))
        else:
            sentence_pieces.append(word)
    sentence = " ".join(sentence_pieces)
    author = current_template["author"]
    # These prints must be inside the function so that the sentence and author match (because the current_template 
    # selected by random.choice is local)
    print(f"Here is your completed famous philosophy quote: {sentence}")
    print("")
    print(f"Author: {author}")

def play_again():
    # This function is a recursion so that you can continue to play as long as you want! 
    affirmatives = {"yes", "oui", "si", "ok", "yeah", "okay", "sure", "please", "aye", "neh"}
        # neh is yes in korean
    response = input("Do you want to play again?").lower().strip() 
    if response in affirmatives:
        mad_libs_sentence()
        play_again()
    elif response == "no":
        print("Thanks for playing")
        # pass exits the program because play_again() is the last thing to be called
        pass
    else:
        print("Type 'yes' to play again or 'no' to quit the program.")
        play_again()


print("Welcome to the Hall of Famous Philosophers Mad Libs Game")
mad_libs_sentence()
print("\n \n")
play_again()