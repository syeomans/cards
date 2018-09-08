from cards import *

# Create deck and shuffle
deck = deck()
deck.shuffle()

leadingCard = None
heartsBroken = False

class player:
	def __init__(self, cardList):
		self.hand = hand(cardList)
		self.tricks = []
		self.numTricks = 0
		self.score = 0

	def takeTrick(self, cardList):
		self.numTricks += 1
		self.tricks.extend(cardList)

	def legalMoves(self):
		
		legalMoves = []

		# If this player is leading the trick
		if leadingCard == None:
			# if hearts have been broken, anything can be played
			if heartsBroken:
				legalMoves = self.hand
			# if hearts haven't been broken, any non-heart can be played
			else:
				for card in self.hand:
					if card.getSuit != "H":
						legalMoves.append(card)

		# If the player is not leading the trick
		else:

			# Add all cards of the same type as the leading card
			for card in self.hand:
				if card.getSuit() == leadingCard.getSuit():
					legalMoves.append(card)

			# If there are no cards of the same type, any card can be played
			if legalMoves == []:
				legalMoves = self.hand

		return(legalMoves)
		


# Create players
player1 = player(deck.deal(13))
player2 = player(deck.deal(13))
player3 = player(deck.deal(13))
player4 = player(deck.deal(13))

player1.hand.printHand()
player2.hand.printHand()
player3.hand.printHand()
player4.hand.printHand()