# ----------------------------------------------------------------------
# This is the file poker.py
#
# In this file, you will write a function that classifies poker hands,
# embedding it in a small application that deals hands and announces
# the type of hand for each player.
#
# Remove ALL of the existing comments in this file prior to submission.
# You can, and should, add your own comments, but please remove all the
# comments that are here now.
#
# Things to do:
#
# This program will make use of the card.py module we created in Lab 11.
#
# In this file, your main program will first ask a user for a numbers
# of players, which should be between 2 and 10. Then it will deal that
# many hands of 5 cards each, using the deal() function from card.py.
# Then, for each hand, it will call a function called classify_hand()
# that you will write, which will classify the hand and return a string
# describing the hand. The classification should be one of the following:
#
#   - "High Card"
#   - "One Pair"
#   - "Two Pair"
#   - "Three of a Kind"
#   - "Straight"
#   - "Flush"
#   - "Full House"
#   - "Four of a Kind"
#   - "Straight Flush"
#   - "Royal Flush"
#
# The classification should be done according to the rules of poker, and
# you can find the rules online or in a book about poker. You should
# use the card.py module to help you with this.
# ----------------------------------------------------------------------

from card import deal_one_five_card_hand, Card

def find_number_of_players(): #returns an integer with the number of players
     while True:
        players = 0 
        try:
           players = int(input("How many players are there?"))
           if players < 2 or players > 10:
               raise ValueError
           else:
                return players 
        except ValueError:
            print("Please enter a valid number between 2 and 10. \n")
            continue

def deal_hands(): # returns a list of dictionaries with 5 Cards (suit, rank) for each player
    players = find_number_of_players()
    hands = []
    [hands.append(deal_one_five_card_hand()) for count in range(players)]
    return hands 

def is_high_card(hand): # returns the card class with the highest rank
    highest_card = None
    for card in hand:
        if highest_card == None:
            highest_card = card
        elif card.rank > highest_card.rank:
            highest_card = card
    return highest_card 

def count_matches(hand, matches_desired): # returns a set of cards that has n number of matches
    for rank in range(13,0,-1):
        counter = 0 
        matches = set()
        for card in hand:
            if rank == card.rank:
                counter += 1
                matches.add(card)
            if counter == matches_desired:
                return matches
    return None

def is_one_pair(hand): # returns a set with the pair of cards that match
    return count_matches(hand, 2) 
            
def three_of_a_kind(hand): # returns a set with the trio of cards that match
    return count_matches(hand, 3)

def hand_to_string(hand): # returns a string of cards in a hand
    cards = set()
    for card in hand:
        cards.add(card.__str__())  
    return ", ".join(cards)

def fake_hand(): # creates a fake hand for testing purposes 
    players = 1
    hands = []
    [hands.append({Card(suit='C', rank=3), Card(suit='D', rank=3), Card(suit="H", rank = 3), 
                   Card(suit='C', rank=7), Card(suit='D', rank=7)}) for count in range(players)]
    return hands 


def classify_hand(): # tests each hand and classifies it to the highest relevant poker hand
    #hands = deal_hands()
    hands = fake_hand()
    for count in range (len(hands)):
        current_hand = hands[count]
        pair = is_one_pair(current_hand)
        trio = three_of_a_kind(current_hand)
        hand_string = hand_to_string(current_hand)
        if trio != None: 
            print(f"Player {count + 1} has three of a kind! From your hand ({hand_string}) the trio is ({hand_to_string(trio)}).")
        elif pair != None:
            print(f"Player {count + 1} has pair! From your hand ({hand_string}) the pair is ({hand_to_string(pair)}).")
        else:
            print(f"Player {count + 1} has a high card. From your hand ({hand_string}) your highest card is", is_high_card(current_hand))

                

classify_hand()



        
        

    



