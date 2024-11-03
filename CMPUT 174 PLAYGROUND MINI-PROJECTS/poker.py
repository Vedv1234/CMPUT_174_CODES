# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my poker game implementation where I've created
# classes for Cards, a Deck, and Poker hands. It's helping me learn about
# object-oriented programming and card game logic.

import random

class Card:
    # My Card class represents a single playing card
    def __init__(self, suit, rank):
        # Setting up my card's basic properties
        self.suit = suit
        self.rank = rank
        
    def get_suit(self):
        # Returns the card's suit (D, H, S, C)
        return self.suit

    def get_rank(self):
        # Returns the card's rank (A, 2-10, J, Q, K)
        return self.rank

    def get_rank_value(self):
        # I'm converting face cards and aces to numerical values
        ranks = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                '8': 8, '9': 9, 'X': 10, 'J': 11, 'Q': 12, 'K': 13}
        return ranks[self.rank]

class Deck:
    def __init__(self):
        # Creating my deck with all 52 cards
        self.deck = []
        suit_list = ['D', 'H', 'S', 'C']  # Diamond, Heart, Spade, Club
        rank_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K']
        
        # Making each possible card combination
        for suit in suit_list:
            for rank in rank_list:
                a_card = Card(suit, rank)
                self.deck.append(a_card)
    
    def shuffle(self):
        # Shuffling my deck randomly
        random.shuffle(self.deck)
        
    def deal(self):
        # Taking a card from the top of my deck
        return self.deck.pop()

class Poker:
    def __init__(self):
        # Starting with an empty hand
        self.hand = []
        
    def add(self, card):
        # Adding a new card to my hand
        self.hand.append(card)
        
    def check_flush(self) -> bool:
        # Checking if I have a flush (all same suit)
        card_suits = {}
        for card in self.hand:
            suit = card.get_suit()
            card_suits[suit] = card_suits.get(suit, 0) + 1
            
        return len(self.hand) in card_suits.values()
    
    def __str__(self):
        # My fancy card display with ASCII art
        string = f'{"+---" * len(self.hand)}\n'
        string = f'{string} |'
        for card in self.hand:
            string = f'{string} {card.get_rank()} |'
        string = f'{string}\n'
        for card in self.hand:
            string = f'{string} {card.get_suit()} |'
        string = f'{string}\n'
        string = f'{string}{"+---" * len(self.hand)}'
        return string

def main():
    # Testing my poker game
    deck = Deck()
    player_hand = Poker()
    
    # Shuffling and dealing 5 cards
    deck.shuffle()
    for i in range(5):
        card = deck.deal()
        player_hand.add(card)
    
    # Showing the hand (uses my __str__ method)
    print(player_hand)

main()