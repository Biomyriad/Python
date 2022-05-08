import random
from os import system, name
from classes.deck import Deck
from classes.card import Card
from classes.hand import Hand

# There is a lot more than can be done to polish this game.
# Like adding a Game class, player and dealer class.
# Also implamenting beting and payouts. At that time maybe I
# would have found a proper use for static and class methods.
# At this stage in the app I don't see a good use for them that
# would make logical since. I am going to discontinue work on this
# as it has already taken up too much time.

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def show_card_table():
    clear()
    dealer_hand.show_cards()
    player_hand.show_cards()
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

    player_hand = Hand()
    player_bust = False
    dealer_hand = Hand()
    dealer_bust = False

    deal_round(dealer_hand, player_hand)

    while not player_bust:
        match input("(H)it, (S)and: "):
            case "h":
                deal_next(player_hand)
            case "s":
                break
        if player_hand.hand_points() > 21:
            player_bust = True

    dealer_hand.hand[0].is_face_down = False
    show_card_table()

    while not dealer_bust:
        if dealer_hand.hand_points() < 17:
            deal_next(dealer_hand)
        else:
            break
        if dealer_hand.hand_points() > 21:
            dealer_bust = True

    show_card_table()

    if player_bust and dealer_bust:
        print("Tie game!")
    elif player_bust and not dealer_bust:
        print("House won!")
    elif not player_bust and dealer_bust:
        print("You won!")
    elif player_hand.hand_points() > dealer_hand.hand_points():
        print("Your won!")
    elif player_hand.hand_points() < dealer_hand.hand_points():
        print("House won!")
    elif player_hand.hand_points() == dealer_hand.hand_points():
        print("Tie game!")
    elif player_hand.hand_points() == 21 and dealer_hand.hand_points() < 21:
        print("BlackJack!")

    if input("Play again? (Y/N): ") == "n":
        end_game = True
    clear()
