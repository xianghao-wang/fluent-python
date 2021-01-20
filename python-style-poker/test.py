from ordered_poker import FrenchDeck
from random import choice

deck = FrenchDeck()

# Choose a card randomly
print(choice(deck))

# Choose several cards
print(deck[:3])

print(deck[12::13])

# Iterate
for card in deck:
    print(card)

# Sort
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)