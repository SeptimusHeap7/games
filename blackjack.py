# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
global in_play, outcome, score
in_play = False
outcome = ""
score = 0
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                          CARD_SIZE)


# define hand class
class Hand:
    cards = []

    def __init__(self):
        self.cards = []

    def __str__(self):
        ans = "Hand Contains:"
        for i in range(len(self.cards)):
            c = self.cards[i]
            ans += c.__str__() + ' '
        return ans

    def add_card(self, card):
        self.cards.append(card)  # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        result = 0
        isAce = False
        for c in self.cards:
            rank = c.get_rank()
            if rank == 'A':
                isAce = True  # compute the value of the hand, see Blackjack video
            value = VALUES[rank]
            result = result + value
        print
        isAce
        if isAce and (result + 10 <= 21):
            result = result + 10
        # print result
        return result

    def draw(self, canvas, pos):
        cardpos = pos
        for card in self.cards:
            card.draw(canvas, cardpos)
            cardpos = pos[0] + CARD_SIZE[0]
            # draw a hand on the canvas, use the draw method for cards


# define deck class
class Deck:
    all_cards = []

    def __init__(self):
        self.all_cards = []  # create a Deck object
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                card = Card(SUITS[i], RANKS[j])
                self.all_cards.append(card)

    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.all_cards)

    def deal_card(self):
        return self.all_cards.pop(0)  # deal a card object from the deck

    def __str__(self):
        ans = "Deck Contains:"
        for i in range(len(self.all_cards)):
            c = self.all_cards[i]
            ans += c.__str__() + ' '
        return ans  # return a string representing the deck


# global var
deck = Deck()
player_hand = Hand()
dealer_hand = Hand()


# define event handlers for buttons
def deal():
    global outcome, in_play
    deck.shuffle()

    c = deck.deal_card()
    player_hand.add_card(c)
    c = deck.deal_card()
    player_hand.add_card(c)
    print
    'player hand: ' + player_hand.__str__()
    player_hand.get_value()

    c = deck.deal_card()
    dealer_hand.add_card(c)
    c = deck.deal_card()
    dealer_hand.add_card(c)
    print
    'dealer hand' + dealer_hand.__str__()
    dealer_hand.get_value()

    in_play = True


def dealer_hit():
    global in_play, outcome, score
    if in_play == True:

        c = deck.deal_card()
        dealer_hand.add_card(c)
        val = dealer_hand.get_value()
        print
        'dealer hand: ' + dealer_hand.__str__()
        print
        'dealer value: ' + str(val)
        if val > 21:
            outcome = 'You win!'
            print
            outcome
            score = score + 1
            in_play = False
        elif val >= 17:
            if player_hand.get_value() > val:
                outcome = 'You win!'
                print
                outcome
                in_play = False
            else:
                outcome = 'You lose!'
                print
                outcome
                in_play = False
    return val


def hit():
    global in_play, outcome, score
    if in_play == True:

        c = deck.deal_card()
        player_hand.add_card(c)
        val = player_hand.get_value()
        print
        'player hand:' + player_hand.__str__()
        print
        'player value: ' + str(val)
        if val > 21:
            outcome = 'You have busted!'
            print
            outcome
            score = score - 1
            in_play = False
    print
    score
    return score

    # replace with your code below

    # if the hand is in play, hit the player

    # if busted, assign a message to outcome, update in_play and score


def stand():
    # replace with your code below

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    while in_play == True:
        dealer_hit()
    # assign a message to outcome, update in_play and score


# draw handler
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below

    card = Card("S", "A")
    card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()

# remember to review the gradic rubric