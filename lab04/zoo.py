def show_help():
    print("Type 'help' to get a list of all the things you can do")
    print("Type 'see' to get a list of all the animals")
    print("Type 'pet' followed by the animal's name to pet a particular animal")
    print("Type 'bye' to leave the zoo and exit the program")
    print("Type 'feed' followed by the animal's name to feed a particular animal")


def show_all_animals():
    print("The animals in the zoo are:")
    print("• Clover the Bunny 🐇")
    print("• Coco the Baby Goat 🐐")
    print("• Arno the Alligator 🐊")
    print("• Clem the Cat 🐈")
    print("• Larry the Rat 🐀")


def pet_animal(animal):
    if animal == "clover":
        print("Clover is so happy! ❤️")
    elif animal == "coco":
        print("Coco the Baby Goat thanks you! 🥰")
    elif animal == "arno":
        print("Actually, we cannot allow you to pet Arno. ⛔️")
    elif animal == "clem":
        print("Clem the Cat is emitting loud purrs 😻")
    elif animal == "larry":
        print("We recommend you wash your hands after petting Larry, he's a street rat ☣️")
    else:
        print("Sorry, I don't know that animal")

def feed_animal(animal):
    if animal == "clover":
        print("Clover LOVES lettuce! Thank you! 🥬🥬")
    elif animal == "coco":
        print("You spoiled Coco with her favorite treat: carrots 🥕🥕🥕")
    elif animal == "arno":
        print("Ok... You better throw this fish from very far away 🐟")
    elif animal == "clem":
        print("Clem is on a diet but he appreciates the thought 😿")
    elif animal == "larry":
        print("Sorry, we can't let you feed Larry. We don't want him to stay 🛑")
    else:
        print("Sorry, I don't know that animal")



print("Welcome to the Petting Zoo!")
print("Type 'help' to get a list of all the things you can do")
print()


while True:
    response = input("What would you like to do? ").strip().lower()
    if response == "help":
        show_help()
    elif response == "see":
        show_all_animals()
    elif response.startswith("pet "):
        animal = response[4:]
        pet_animal(animal)
    elif response.startswith("feed "):
        animal = response[5:]
        feed_animal(animal)
    elif response == "bye":
        print("Goodbye!")
        break
    else:
        print("Sorry, I don't understand that command")
        