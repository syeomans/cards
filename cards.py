import random

class card:
	def __init__(self, value, suit, aceHigh = True):
		self.value = value
		self.suit = suit
		self.aceHigh = aceHigh
	
	def getNumericValue(self):
		"""
		Returns the numeric value of the card as an integer. 

		Ex: QH (Queen of Hearts) returns 12, 9C (9 of Clubs) returns 9, etc.
		If aceHigh is false, Ace returns 1; else, Ace returns 14
		"""
		if self.value == "J":
			return(11)
		elif self.value == "Q":
			return(12)
		elif self.value == "K":
			return(13)
		elif self.value == "A" and self.aceHigh:
			return(14)
		elif self.value == "A":
			return(1)
		else:
			return(int(self.value))

	def getValue(self):
		return(self.value)

	def getSuit(self):
		return(self.suit)

	def getName(self):
		"""
		Returns the shorthand (two-character) name of the card, which can be used as a 
		unique identifier in a single deck.

		For example, the Queen of Hearts has the name QH
		"""
		return(self.value + self.suit)

class deck:
	def __init__(self):
		self.cards = []
		nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
		suits = ['H', 'D', 'S', 'C']
		for suit in suits:
			for num in nums:
				self.cards.append(card(num, suit))

	def shuffle(self):
		random.shuffle(self.cards)

	def deal(self, numCards):
		returnList = []
		for i in range(0,numCards):
			returnList.append(self.cards.pop())
		return(returnList)

	def add(self, cardList):
		self.cards.extend(cardList)

	def getDeck(self):
		returnList = []
		for card in self.cards:
			returnList.append(card.getName())
		return(returnList)

class hand:
	def __init__(self, cardList = []):
		self.cards = cardList

	def draw(self, cardList):
		self.cards.extend(cardList)

	def play(self, targetCard):
		# If the target card is given as a string, search for the card by name and pop it
		if isinstance(targetCard, str):
			for i in range(0,len(self.cards)):
				if getName(self.cards[i]) == targetCard:
					return(self.cards.pop(i))

		# If the target card is given as an int referencing an index in the hand, pop that reference
		elif isinstance(targetCard, int):
			return(self.cards.pop(targetCard))

	def getHand(self):
		returnList = []
		for card in self.cards:
			returnList.append(card)
		return(returnList)

	def printHand(self):
		returnStr = ''
		for card in self.cards:
			returnStr = returnStr + ", " + card.getName()
		print(returnStr[2:])
