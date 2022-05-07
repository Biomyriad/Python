from . import card

class Hand:
    def __init__(self):
        self.hand = []

    def receive_card(self, card):
        self.hand.append(card)

    def discard_by_index(self, index):
        if len(self.hand) > 0:
            return self.hand.pop(index)
            
    def discard_by_card(self, card):
        if len(self.hand) > 0:
            self.hand.remove(card)

    def hand_points(self):
        num_of_ace = 0
        hand_val = 0

        for card in self.hand:
            if card.point_val == 1 and card.is_face_down == False:
                num_of_ace += 1
        
        for card in self.hand:
            if card.point_val == 1 or card.is_face_down == True:
                continue
            hand_val += card.point_val if card.point_val < 11 else 10
        
        if num_of_ace == 0:
            return hand_val
        
        val = []
        for i in range(0, num_of_ace + 1):
            calc = (num_of_ace - i) + (i * 11)
            if hand_val + calc > 21:
                continue
            val.append(hand_val)

        return val.pop() + calc

    def show_cards(self):
        for card in self.hand:
            print(f"{card.short_card_val()} ", end="")
        
        print(f"|| {self.hand_points()}")
