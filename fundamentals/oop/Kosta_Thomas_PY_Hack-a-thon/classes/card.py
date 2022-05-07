class Card:

    def __init__( self , suit , point_val , string_val, is_face_down=False):
        self.is_face_down = is_face_down
        self.suit = suit
        self.point_val = point_val
        self.string_val = string_val

    def short_card_val(self):
        card_val = ""

        if self.is_face_down:
            return "🂠"

        if self.string_val.isdigit():
            card_val += self.string_val
        else:
            card_val += self.string_val[0]
        
        match self.suit:
            case "spades":
                card_val += "♠"
            case "hearts":
                card_val += "♥"
            case "clubs":
                card_val += "♣"
            case "diamonds":
                card_val += "♦"
        return card_val

    def card_info(self):
        return f"{self.string_val} of {self.suit} : {self.point_val} points"