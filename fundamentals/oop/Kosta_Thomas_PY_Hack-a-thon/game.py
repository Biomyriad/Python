import random
from os import system, name
from classes.deck import Deck
from classes.card import Card
from classes.hand import Hand

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def show_card_table():
    clear()
    d_hand.show_cards()
    p_hand.show_cards()
    print("-----------------")

def deal_round(dealer, player):
    player.receive_card(deck.draw_card())
    dealer.receive_card(deck.draw_card(True))
    player.receive_card(deck.draw_card())
    dealer.receive_card(deck.draw_card())
    show_card_table()


def deal_next(hand):
    hand.receive_card(deck.draw_card())
    show_card_table()

############################
end_game = False
while not end_game:

    deck = Deck()
    deck.shuffle_cards()

    p_hand = Hand()
    p_bust = False
    d_hand = Hand()
    d_bust = False

    deal_round(d_hand, p_hand)

    while not p_bust:
        match input("(H)it, (S)and: "):
            case "h":
                deal_next(p_hand)
            case "s":
                break
        if p_hand.hand_points() > 21:
            p_bust = True

    d_hand.hand[0].is_face_down = False
    show_card_table()

    while not d_bust:
        if d_hand.hand_points() < 17:
            deal_next(d_hand)
        else:
            break
        if d_hand.hand_points() > 21:
            d_bust = True

    show_card_table()

    if input("Play again? (Y/N): ") == "n":
        end_game = True
    clear()
