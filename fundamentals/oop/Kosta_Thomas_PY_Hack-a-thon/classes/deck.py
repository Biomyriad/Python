import random
from . import card

class Deck:
    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []

        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( card.Card( s , i , str_val) )

    def shuffle_cards(self):
        for i in range(0,50):
            random.shuffle(self.cards)

    def draw_card(self, is_face_down=False):
        card = self.cards.pop()
        card.is_face_down = is_face_down
        return card

    def show_cards(self):
        for card in self.cards:
            print(card.short_card_val())

