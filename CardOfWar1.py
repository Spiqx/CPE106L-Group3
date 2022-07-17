
import sys
import random

class PlayCard:
    suits = ['\u2660', '\u2663', '\u2665', '\u2666']
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s %s' % (PlayCard.suits[self.suit], PlayCard.ranks[self.rank])

    def __lt__(self, other):
        t1 = self.rank, self.suit
        t2 = other.rank, other.suit
        return t1 < t2

class DeckOfCards:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                card = PlayCard(suit, rank)
                self.cards.append(card)
        self.shuffle()

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return ', '.join(res)

    def __len__(self):
        return len(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def pop_card(self, i=-1):
        return self.cards.pop(i)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def wincard(self, cards):
        winner = cards[0]
        for card in cards:
            if winner < card:
                winner = card
        return winner

class PlayerHand(DeckOfCards):

    def __init__(self, label=''):
        self.cards = []
        self.label = label
        self.wincount = 0

    def getlabel(self):
        return self.label

    def roundwinner(self):
        self.wincount += 1

    def getwincount(self):
        return self.wincount

    def __str__(self):
        return "Playing cards for " + self.label + " are " + DeckOfCards.__str__(self)

def play(argv):
    deck = DeckOfCards()
    hands = []
    for i in range(1, 5):
        player = 'Contender %d' % i  
        if len(argv) > i:
            player = argv[i]  
        hands.append(PlayerHand(player))  

    while len(deck) > 0:
        for hand in hands:
            hand.add_card(deck.pop_card())  

    print(hands[0])  
    input("Welcome to Card of War!. Press and enter any key to start playing: ")  

    for i in range(1, 14):
        cards = []  
        levels = []  
        for hand in hands:
            card = hand.pop_card()
            cards.append(card)  
            levels.append(hand.getlabel() + " : " + str(card))  

        winner_card = deck.wincard(cards)  
        winner_hand = hands[cards.index(winner_card)]  
        winner_hand.roundwinner()  
        print("Round", i, ":-", ", ".join(levels), ", Victor :- ", winner_hand.getlabel(), ":", winner_card)
        input()  

    for hand in hands:  
        print("Points for our", hand.getlabel(), "is", hand.getwincount())

def main(argv=[]):
    answer = "Y"
    while answer.upper() == "Y":
        play(argv)
        answer = input("Do you want to play again (Y/N)?: ")
    print("Thank you for playing the game!")

if __name__ == '__main__':
    main(sys.argv)
