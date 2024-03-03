"""
Kangning Li
CS 5001 Spring 2024
cards.py
"""
import random


def create_deck() -> list:
    """
    this function creates a deck of 52 cards
    """
    first = ['2', '3', '4', '5', '6',
             '7', '8', '9', 'T', 'J',
             'Q', 'K', 'A']
    second = ['s', 'h', 'd', 'c']
    deck = []

    for letter2 in second:
        for letter1 in first:
            deck.append(letter1 + letter2)
            
    return deck

def shuffle(cards: list) -> list:
    """
    this function shuffle the 52 cards
    and return a new list of cards
    """
    original = cards.copy()
    shuffled_cards = []
    
    # randomly pick a card from cards and put it into new list
    while len(original) != 0:
        card = original.pop(random.randint(0, len(original) - 1))
        shuffled_cards.append(card)

    return shuffled_cards

def deal(number_of_hands: int, number_of_cards: int,
         cards: list) -> list:
    """
    this function takes the numbers of hands (up to 4),
    number of cards per hand (up to 13),
    and the deck of cards to deal from
    return a list containing all of the hands
    that were dealt
    """
    deal_cards = []

    for hand in range(number_of_hands):
        # empty list for card on the hand
        card_in_hand = []
        for i in range(number_of_cards):
            # get a card from original list to the hand
            card_in_hand.append(cards.pop())
        # every hand construct new hand in list
        deal_cards.append(card_in_hand)

    return deal_cards

def main():
    # Test Code
    print("Original deck is:")
    deck = create_deck()
    print(deck)
    print("")

    print("The shuffled deck is:")
    deck = shuffle(deck)
    print(deck)
    print("")

    print("Dealt one round of 4 players")
    print(deal(4, 2, deck))
    print("")

    print("Cards left in deck")
    print(deck)
    print("")
    

if __name__ == "__main__":
    main()
