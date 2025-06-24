from card import deal, poker_classification

hand_size = 5

def find_number_of_players(): #returns an integer with the number of players
     while True:
        user_input = input("Enter the number of players(2-10):").strip().lower()
        match user_input:
            case "bye": 
                raise SystemExit 
            case "exit": 
                raise SystemExit
            case players if user_input.isdigit():
                if int(players) < 2 or int(players) > 10: 
                    print("Please enter a valid number between 2 and 10. \n")   
                else:
                    return int(players)
            case _:
                print("Please enter a valid number between 2 and 10. \n")


def hand_to_string(hand): # returns a string of cards in a hand
    cards = set()
    for card in hand:
        cards.add(card.__str__())  
    return ", ".join(cards)

def classify_hand(): # tests each hand and classifies it to the highest relevant poker hand then prints the hand and it's classification
    hands = deal(cards_per_hand= hand_size, number_of_hands= find_number_of_players())
    for count in range (len(hands)):
        current_hand = hands[count]   
        print(f"{hand_to_string(current_hand)} is a {poker_classification(current_hand)}")

classify_hand()