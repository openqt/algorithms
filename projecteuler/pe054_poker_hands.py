# coding=utf-8
"""
Poker hands
Problem 54

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
    2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example 1
below). But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below); if the
highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

    Hand        Player 1        Player 2	 	    Winner
    1	 	5H 5C 6S 7S KD      2C 3S 8S 8D TD      Player 2
            Pair of Fives       Pair of Eights

    2	 	5D 8C 9S JS AC      2C 5C 7D 8S QH      Player 1
            Highest card Ace    Highest card Queen

    3	 	2D 9C AS AH AC      3D 6D 7D TD QD      Player 2
            Three Aces          Flush with Diamonds

    4	 	4D 6S 9H QH QC      3D 6D 7H QD QS      Player 1
            Pair of Queens      Pair of Queens
            Highest card Nine   Highest card Seven

    5	 	2H 2D 4C 4D 4S      3C 3D 3S 9S 9D      Player 1
            Full House          Full House
            With Three Fours    with Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You can
assume that all hands are valid (no invalid characters or repeated cards), each
player's hand is in no specific order, and in each hand there is a clear
winner.

How many hands does Player 1 win?
"""
from __future__ import print_function


class FiveCard(object):
    """Internal five card data"""
    MAP = {
        'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14,
        10: 'T', 11: 'J', 12: 'Q', 13: 'K', 14: 'A',  # reverse lookup
    }

    def __init__(self, cards=None):
        if cards:
            self.set(cards)

    def set(self, cards):
        """build internal data structure

        :param cards: as 5H 5C 6S 7S KD
        """
        if isinstance(cards, str):
            cards = cards.split()

        val = {}
        for card in cards:
            v = FiveCard.MAP.get(card[0]) or int(card[0])
            s = card[1]

            if v not in val:
                val[v] = ''
            val[v] += s
        self.values = sorted(val.items())

        self.suits = {}
        for i in self.values:
            self.suits.setdefault(len(i[1]), []).append(i[0])

        return self

    def __str__(self):
        s = ''
        for val, suits in self.values:
            for suit in suits:
                s += FiveCard.MAP.get(val) or str(val)
                s += suit + ' '
        return s

    def __repr__(self):
        return repr(self.values) + ' <=> ' + repr(self.suits)

    @property
    def high_card(self):
        """Highest value card."""
        return self.suits[1][-1]

    @property
    def one_pair(self):
        """Two cards of the same value."""
        if 2 in self.suits:
            return self.suits[2][-1]
        return None

    @property
    def two_pair(self):
        """Two different pairs."""
        if 2 in self.suits and len(self.suits[2]) == 2:
            return sorted(self.suits[2], reverse=True)
        return None

    @property
    def three_kind(self):
        """Three cards of the same value."""
        if 3 in self.suits:
            return self.suits[3][0]
        return None

    @property
    def straight(self):
        """All cards are consecutive values."""
        if len(self.suits) == 1 \
                and self.values[-1][0] - self.values[0][0] == 4:
            return self.high_card
        return None

    @property
    def flush(self):
        """All cards of the same suit."""
        suit = self.values[0][1]
        for val in self.values:
            for s in val[1]:
                if s != suit:
                    return None
        return self.high_card

    @property
    def full_house(self):
        """Three of a kind and a pair."""
        if sorted(self.suits) == [2, 3]:
            return self.suits[3][-1], self.suits[2][-1]
        return None

    @property
    def four_kind(self):
        """Four cards of the same value."""
        if 4 in self.suits:
            return self.suits[4][0]
        return None

    @property
    def straight_flush(self):
        """All cards are consecutive values of same suit."""
        if self.flush:
            return self.straight
        return None

    @property
    def royal_flush(self):
        """ Ten, Jack, Queen, King, Ace, in same suit."""
        if self.flush and self.straight == 14:
            return self.straight
        return None


def rank(p1, p2):
    for n in ['royal_flush',
              'straight_flush',
              'four_kind',
              'full_house',
              'flush',
              'straight',
              'three_kind',
              'two_pair',
              'one_pair',
              'high_card']:
        c = cmp(getattr(p1, n), getattr(p2, n))
        if c != 0:
            return c
    return 0


if __name__ == '__main__':
    print(rank(FiveCard('5H 5C 6S 7S KD'), FiveCard('2C 3S 8S 8D TD')))  # -1
    print(rank(FiveCard('5D 8C 9S JS AC'), FiveCard('2C 5C 7D 8S QH')))  # 1
    print(rank(FiveCard('2D 9C AS AH AC'), FiveCard('3D 6D 7D TD QD')))  # -1
    print(rank(FiveCard('4D 6S 9H QH QC'), FiveCard('3D 6D 7H QD QS')))  # 1
    print(rank(FiveCard('2H 2D 4C 4D 4S'), FiveCard('3C 3D 3S 9S 9D')))  # 1

    count = 0
    with open('data/p054_poker.txt') as f:
        for i in f:
            data = i.split()
            if data and rank(FiveCard(data[:5]), FiveCard(data[5:])) > 0:
                count += 1
    print(count)  # 376

    # Another way is give a score for each hand then simply compare the values
