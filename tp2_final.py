"""TDLOG TP2 - Pauline MOLITOR, Ilyass RAMDANI - 3,5 brain hours"""

import random

_LIMIT = '+-----|-----+'
"""The top and bottom lines of a domino representation"""


_DOTS = [
    ['     ', '     ', '     '],
    ['     ', '  *  ', '     '],
    ['*    ', '     ', '    *'],
    ['*    ', '  *  ', '    *'],
    ['*   *', '     ', '*   *'],
    ['*   *', '  *  ', '*   *'],
    ['* * *', '     ', '* * *']]
"""The dots lines of a domino representation"""

class Domino:
    """Class representing a domino with its left and right numbers. """
    def __init__ (self, left0, right0):
        self._left = left0
        self._right = right0

    @property
    def left(self):
        """Return the left property of a domino"""
        return self._left

    @property
    def right(self):
        """Return the right property of a domino"""
        return self._right

    def __repr__(self):
        result = "Domino("+str(self.left)+", "+str(self.right)+")"
        return result

    def __str__(self):
        # build the domino representation line by line
        result = '\n'.join([
            _LIMIT,
            '|' + _DOTS[self.left][0] + '|' + _DOTS[self.right][0] + '|',
            '|' + _DOTS[self.left][1] + '|' + _DOTS[self.right][1] + '|',
            '|' + _DOTS[self.left][2] + '|' + _DOTS[self.right][2] + '|',
            _LIMIT]) + '\n'
        return result

    def __eq__(self, other):
        return ((self.left == other.left and self.right == other.right)
                or (self.left == other.right and self.right == other.left))

    def __ne__(self, other):
        return (not ((self.left == other.left and self.right == other.right)
                or (self.left == other.right and self.right == other.left)))


DOMINOS_SET = [Domino(left, right) for left in range(7) for right in range(left + 1)]
"""The 28 dominos in the game"""


HAND_SIZE = 7
"""Number of dominos in the hand"""


TARGET = 12
"""Number of points on dominos to discard them"""

class Solitaire:
    """Class representing a solitaire game with a pile of dominoes and the player's hand"""
    def __init__(self):
        self.pile = random.sample(DOMINOS_SET, len(DOMINOS_SET))
        self.hand = []
        self.is_over = False

    def is_game_won(self):
        """Return true iff the game is over and the player won"""
        return self.is_over and (not self.hand)

    def is_game_lost(self):
        """Return True iff the game is over and the player lost"""
        return self.is_over and self.hand

    def turn(self):
        """Implement one turn of the game. \
            Return 0 if nothing went wrong and 1 if the indexes are not valid"""
        # fill the hand with HAND_SIZE dominos until the pile is empty
        while len(self.hand) != HAND_SIZE and self.pile:
            self.hand.append(self.pile.pop())

        # check if the game is won (the hand and the pile are empty)
        if not self.hand:
            self.is_over = True
            return 0

        # print the dominos hand and ask the player to play
        for (i, domino) in enumerate(self.hand):
            print (f'Domino {i+1}:')
            print(domino)
        indexes = input(
            f'pile size = {len(self.pile)}, dominos to discard?'
            f" (if you don 't have any valid combination enter ' q ')")

        # if the player doesn't find any valid combination, the game is over
        if indexes == 'q':
            self.is_over = True
            return 0

        # count the sum of the selected dominos
        try:
            indexes = sorted(
                [int(idx) - 1 for idx in indexes], reverse=True)
            total = sum(self.hand[idx].left + self.hand[idx].right for idx in indexes)
        except (ValueError, IndexError):
            print('invalid indexes')
            return 1

        # If the total is correct, discard the selected dominos
        if  total != TARGET:
            print(f'invalid total ({total} but expected {TARGET})')
        else:
            for idx in indexes:
                self.hand.pop(idx)

    def play(self):
        """Run the game until it's over"""
        while not self.is_over:
            self.turn()
        if self.is_game_won():
            print("You win!")
        else:
            print("You lose...")

def main():
    """Entry point of the program, run some test on the domino's methods \
        and then run a domino game"""
    # part 1
    domino1 = Domino(3, 5)
    domino2 = Domino(3, 5)
    domino3 = Domino(2, 4)
    # test of __repr__ and __str__
    print (repr(domino1))
    print(domino1)
    # test of __eq__ and __ne__
    print(domino1 == domino2)
    print(domino1 == domino3)
    print(domino1 != domino2)
    print(domino1 != domino3)

    # part 2
    game = Solitaire()
    # launch of the game
    game.play()


if __name__ == '__main__':
    main()
