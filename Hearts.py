from cards import *

class player:
	def __init__(self, cardList):
		self.hand = hand(cardList)
		self.tricks = []
		self.numTricks = 0
		self.score = 0
		self.has2C = query2C()

	def query2C(self):
		thisHand = self.hand.getHand()
		for card in thisHand:
			if card.getName() == "2C":
				return(True)
		return(False)

	def takeTrick(self, cardList):
		self.numTricks += 1
		self.tricks.extend(cardList)

	def legalMoves(self):
		
		thisHand = self.hand.getHand()
		legalMoves = []

		# If this player is leading the trick
		if leadingCard == None:
			# if hearts have been broken, anything can be played
			if heartsBroken:
				for card in thisHand:
					legalMoves.append(card.getName())
			# if hearts haven't been broken, any non-heart can be played
			else:
				for card in thisHand:
					if card.getSuit() != "H":
						legalMoves.append(card.getName())

		# If the player is not leading the trick
		else:

			# Add all cards of the same type as the leading card
			for card in thisHand:
				if card.getSuit() == leadingCard.getSuit():
					legalMoves.append(card.getName())

			# If there are no cards of the same type, any card can be played
			if legalMoves == []:
				for card in thisHand:
					legalMoves.append(card.getName())
		return(legalMoves)

		def selectCard(self):
			moves = self.legalMoves()
			return(legalMoves[randint(0,len(moves))])


	def play(self, cardName):
		return(self.hand.play(cardName))

# Create deck and shuffle
deck = deck()
deck.shuffle()
		
# Create players
players = [player(deck.deal(13)) for i in range(0,4)]

# Initialize global variables
leadingCard = '2C'
heartsBroken = False
tookLastTrick = 0 # integer 0-3, representing which player took the last trick
playing = True

# Player with 2C leads first trick
for player in players:
	if player.query2C() == True:
		player.play('2C')
		break
	tookLastTrick += 1


leadingCard = None # For test purposes, the leading card has not been chosen. 
# Second trick and onward
while playing:
	# Start from the player who took the last trick
	for i in [tookLastTrick, (tookLastTrick+1)%4, (tookLastTrick+2)%4, (tookLastTrick+3)%4]:
		# Make a move
		move = players[i].selectCard()
		# If the player is leading the trick, record the card (s)he played. 
		if i == tookLastTrick:
			leadingCard = move.getName()







# Test script
players[0].hand.printHand()
print(players[0].legalMoves())