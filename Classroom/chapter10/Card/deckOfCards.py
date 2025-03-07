from card import Card
import random

class DeckOfCards:
    number_of_cards = 52
    def __init__(self):
        self.current_card = 0
        self.list_card = []
        for index in range (DeckOfCards.number_of_cards):
            face = Card.FACES[index%13]
            suit = Card.SUITS[index//13]
            self.list_card.append(Card(face, suit))

    def dealCard(self):
        card = self.list_card[self.current_card]
        self.current_card += 1
        try:
            return card
        except IndexError:
            return None
    
    def shuffleDeck(self):
        random.shuffle(self.list_card)
    
    def __str__(self):
        cards = ''
        for i in range(52):
            cards += f'{str(self.list_card[i]):<20}'
            if(i + 1)%4 == 0:
                cards += '\n'
        return cards


# deck = DeckOfCards()
# print(deck)

# deck.shuffleDeck()
# print(deck)