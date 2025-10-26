from sys import setdlopenflags
from typing import NamedTuple
import random

class Card(NamedTuple):
    rank: str
    suit: str

    def __eq__(self, othercard):

        if self.rank == othercard.rank and self.suit == othercard.suit:
          return True

        return False

    def __lt__(self, otherCard):
        # create a list of the order of the cards
        order = []
        for val in range(2, 11):
            order.append(str(val))
        order += ["J", "Q", "K", "A"]
        
        return order.index(self.rank) < order.index(otherCard.rank)
        
class Deck:

    def __init__(self):
        self.card_list = []

        # For the 4 suits
        for suit in "HDCS":

            # Create all the 2-10 cards
            for rank in range(2, 11):
                c = Card(str(rank), suit)
                self.card_list.append(c)
            
            # Create the face cards
            for rank in "JQKA":
                c = Card(rank, suit)
                self.card_list.append(c)
    
    def __str__(self):
        outS = []
        
        for card in self.card_list:
            outS.append(card.rank + card.suit)

        return ", ".join(outS)
    
    def __getitem__(self, x):
        return self.card_list[x]

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.card_list)
    
    def top(self):
        return self[0]

    def bottom(self):
        return self.card_list[-1]

    def get_n(self, n):
        return self[n]

    def get_random(self):
        '''
        i = random.randint(0, len(self.card_list))

        return self.get_n(i)
        '''
        return random.choice(self.card_list)
    
    def shuffle(self):
        random.shuffle(self.card_list)

    def get_stack(self, start, end):
        '''
        Return a list of cards from location start to         location end
        '''
        return self[start: end+1]
    
    def reverse(self):
        outS = []
        
        for card in reversed(self.card_list):
            outS.append(card.rank + card.suit)

        return ", ".join(outS)
    
    def index(self, rank, suit):
        for card in self.card_list:
            if (card.rank == rank) and (card.suit == suit):
                return self.card_list.index(card)
        return None
    
    def cut(self, index):
        new_deck = self.card_list[index::] + self.card_list[:index]

        outS = []
        
        for card in new_deck:
            outS.append(card.rank + card.suit)

        return ", ".join(outS)
    
    def pop(self):
        removed = self.card_list[0]
        self.card_list.remove(self.card_list[0])
        return removed.rank + removed.suit
    
    def draw(self, n):
        drawn = []
        for card in range(n):
            drawn.append(self.card_list[card].rank + self.card_list[card].suit)
        self.card_list = self.card_list[n::]
        return drawn
    
    def sort(self):
        rank_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        suit_order = {'H': 0, 'D': 1, 'C': 2, 'S': 3}

        self.card_list.sort(key=lambda card: (suit_order[card.suit], rank_order[card.rank]))




thedeck = Deck()
print(thedeck)
thedeck.shuffle()
print(thedeck)
thedeck.sort()
print(thedeck)