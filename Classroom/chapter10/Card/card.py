#card.py

class Card:
    FACES = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    SUITS = ['Hearts', 'Spades', 'Clubs', 'Diamonds']

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def image_name(self):
        return str(self).replace(' ', '_')+'.png'
    
    def __str__(self):
        return f"{self.face} of {self.suit}"
