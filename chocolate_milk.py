
import random
class Die:
    def __init__(self, number_sides):
        self. num_sides = number_sides
        self.face_up = None
    def roll_die(self):
        self.face_up = random.randint(1, self.num_sides)

diel = Die (6)
diel.roll_die()
print(diel.face_up)


class Card:
    def __init__(self, card_val, card_suit):
        self.value = card_val
        self.suit = card_suit
    def desc(self): 
        val_name = self.value
        if self.value == 1:
            val_name = "Ace"
        elif self.value == 11:
            val_name = "jack"
        elif self.value == 12:
            val_name = "queen"
        elif self.value == 13:
            val_name = "king"
        return f"{val_name} of {self.suit}" 
    def print(self):
        print(self.desc())

card1 = Card(9, "Diamonds")
card2 = Card(1, "hearts")
card3 = Card(13, "spades")
card1.print()
card2.print()
card3.print()





class Deck:
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        self.cards = []
        for s in ["Clubs", "Hearts", "Spades", "Diamonds"]:
            for i in range(1,14):
                self.cards.append(Card(i, s))
        


    def shuffle(self):
        random.shuffle(self.cards)

    def print_deck(self):

        for c in self.cards: 
            c.print()

    
    
    
    
    
    
    
    def deal(self, num_players, hand_size):
        list_of_hands = []
        for i in range(num_player):
            hand_cards = []
            for j in range(hand_size):
                hands_cards.append(self.cards.pop(0))
            list_of_hands.append(hand_cards)
        return list_of _hands

deck1 = Deck()
deck1 = shuffle()
deck1 = print_deck()
hands = deck1.deal(3, 7)
for hand in hands:
    print("\nplayer's cards")
    for c in hand:
        c.print()
        
class Chocolatemilk:
    def __init__(self, list_of_player_names, hand size):

        self.num_players
        self.players
        self.hand_size
        self.die1 = Die(6)
        self.die2 = Die(6)

        self.deck = Deck
        self.deck.shuffle()
        self.players_hands = {}
        self. deal()

    def deal(self):
        dealt_cards = self.deck.deal(self.num_players, self.hand_size)
        self.players_hands = dict(zip (self.players, dealt_cards))

    def roll (self):
        self.die1.roll_die()
        self.die2.roll_die()


        def current_dice_sum(self):
            return self.die1.face_up + self.die2. face_up

        def print_hand(self, player_name):
            print(f"{count}: ",end = '')
            c.print()
            count += 1

    def run_one_turn(self, player_name):
        print(f"")


d
        
deck1 = Deck()
deck1.shuffle()
deck1.pDeckrint_deck()














