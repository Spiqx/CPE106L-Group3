from CardOfWar1 import DeckOfCards
from CardOfWar3 import Contender

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