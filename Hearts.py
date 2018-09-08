from cards import *

# Create deck and shuffle
deck = deck()
deck.shuffle()

class player:
	def __init__(self, cardList):
		self.hand = hand(cardList)
		self.tricks = []
		self.numTricks = 0
		self.score = 0

	def takeTrick(cardList):
		self.numTricks += 1
		self.tricks.extend(cardList)


# Create players
player1 = player(deck.deal(13))
player2 = player(deck.deal(13))
player3 = player(deck.deal(13))
player4 = player(deck.deal(13))

player1.hand.printHand()
player2.hand.printHand()
player3.hand.printHand()
player4.hand.printHand()