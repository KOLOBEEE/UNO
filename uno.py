

import random 

def cards_per_player():
    while True:
        cards_on_hand = input("enter number of cards: ")
        if cards_on_hand.isdigit():
                cards_on_hand = int(cards_on_hand)
                if cards_on_hand == 7:
                   break
                elif cards_on_hand < 7:
                   print("number of cards lower.")
                elif cards_on_hand > 7:
                   print("number of cards higher.")
                else:
                   print("number of cards is a number.")
        else:
            print("number of cards is a number.")

    
    return cards_on_hand
cards_per_player()
        


def cardDeck():
    card_colour = ["red", "blue", "yellow", "green"]
    card_value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw Two", "Reverse card", "skip"]
    wilds = ["wild", "wild two", "wild draw four"]
    deck = []

    for colour in card_colour:
        for value in card_value:
                cardValue = "{} {}".format(colour, value)
                deck.append(cardValue)
                if value !=0:
                     deck.append(cardValue)

    for i in range(4):
         deck.append(wilds[0])
         deck.append(wilds[1])

        
    
    print(deck)
    return deck


cardDeck()

def ShuffleDeck(deck):
    for cardPos in range(len(deck)):
        randPos = random.randint(0,107)
        deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]

    return deck


#def drawCards():
      
     

UnoDeck = cardDeck()
UnoDeck = ShuffleDeck(UnoDeck)
print(UnoDeck)