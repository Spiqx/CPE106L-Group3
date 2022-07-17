from random import shuffle

class PlayCard:
    suits = ["\u2660", "\u2663", "\u2665", "\u2666"]

    ranks = [None, None,"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, r, s):
        self.rank = r
        self.suit = s

    def __lt__(self, c2):
        if self.rank < c2.rank:
            return True
        if self.rank == c2.rank:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.rank > c2.rank:
            return True
        if self.rank == c2.rank:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        r = self.ranks[self.rank] +\
            " of " + \
            self.suits[self.suit]
        return r

class DeckOfCards:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards\
                    .append(PlayCard(i,j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Contender:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class CardGame:
    def __init__(self):
        name1 = input("contender 1 name ")
        name2 = input("contender 2 name ")
        self.deck = DeckOfCards()
        self.p1 = Contender(name1)
        self.p2 = Contender(name2)

    def wins(self, winner):
        w = "{} is the victor for this round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} picked {} while {} picked {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("The war begins! Get ready")
        while len(cards) >= 2:
            m = "Press f to exit the game. Press and enter any " + \
            "key to continue playing:"
            response = input(m)
            if response == 'f':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print("The war has ended. {} is the victor" .format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "There was a tie among the contenders! No one"

game = CardGame()
game.play_game()
