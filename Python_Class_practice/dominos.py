# Consider a 6 * 6 grid:
# Imagine I start painting dominos onto the grid. By a domino, I mean that I paint two adjacent squares (one should be directly above, below, to the left or to the right of the other, not diagonal).
# Suppose that I paint multiple dominos, one after another, in random locations. For each new domino that I paint, I choose two random unoccupied adjacent squares in the grid (with each possible valid placement being equally likely).
# If I keep doing this for long enough, I will eventually run out of places where I can paint dominos either because I paint all 36 squares, or because I end up in a situation where there are no pairs of adjacent empty squares remaining.
#
# Question: if I paint dominos on the grid randomly until I can't paint any more, what is the probability that I will end up painting all 36 squares?
# game() is a game asking the user to fill every space of the board with dominos, starting with two random placed dominos.

import random

class Board:
    def __init__(self):
        '''Create and initialize a 6×6 board.'''
        self._board = []
        for _ in range(6):
            self._board.append(['.'] * 6)
        self._num_dominos = 0
        self._choice = list(range(60))

    def dominos(self):
        return self._num_dominos

    def display(self):
        '''Display what the board looks like. '''
        for i in range(6):
            for j in range(6):
                print(self._board[i][j], end = '')
            print('')
        print('')

    def eligible(self,i,j):
        '''
        Determine if (i,j) on the board is eligble for placing a domino.
        '''
        self._i_isinrange = i>=0 and i<=5
        self._j_isinrange = j>=0 and j<=5
        return self._i_isinrange and self._j_isinrange and self._board[i][j] == '.'

    def _txy2n(self,t,x,y):
        '''This function converts t,x,y to n for internal use'''
        return 2*(6*y + x) + t

    def paint(self,x1,y1,x2,y2):
        '''
        Try and paint (x1,y1) and (x2,y2). If not able to do so, return False.
        '''
        if self.eligible(x1,y1) and self.eligible(x2,y2):
            if x1 == x2 and abs(y1-y2) == 1:
                self._t = 1
                self._x = x1
                self._y = min(y1,y2)
            elif abs(x1-x2) == 1 and y1 == y2:
                self._t = 0
                self._x = y1
                self._y = min(x1,x2)
            else:
                print('The twos squares being painted is not adjacent.')
                return False
            self._board[x1][y1] = 'P'
            self._board[x2][y2] = 'P'
            self._num_dominos += 1
            self.update()
            return True
        else:
            print('You can\'t put it there.')
            return False

    def update(self):
        '''
        After placing a domino, update the choices a domino can be placed.
        i.e. Some n are to be disabled, so we remove them from self._choice
        Since they may have been removed already, we use try here.
        '''
        self._choice.remove(self._txy2n(self._t,self._x,self._y))
        if self._y > 0:
            #Can't use the left space as horizontal head
            try:
                self._choice.remove(self._txy2n(self._t,self._x,self._y-1))
            except:
                # If it is already removed we get an error, but no need to act.
                pass
        if self._y < 4:
            #Can't use the right space as horizontal head
            try:
                self._choice.remove(self._txy2n(self._t,self._x,self._y+1))
            except:
                pass
        if self._x > 0:
            #Can't use the space above as vertical head
            try:
                self._choice.remove(self._txy2n(1-self._t,self._y,self._x-1))
            except:
                pass
            try:
                self._choice.remove(self._txy2n(1-self._t,self._y+1,self._x-1))
            except:
                pass
        if self._x < 5:
            #Can't use the space as vertical head
            try:
                self._choice.remove(self._txy2n(1-self._t,self._y,self._x))
            except:
                pass
            try:
                self._choice.remove(self._txy2n(1-self._t,self._y+1,self._x))
            except:
                pass

    def random_paint(self):
        '''
        Try to place a domino randomly on the board.
        How to make sure that random_paint() certainly works:
        1. Divide the dominos into two types: vertical and horizontal.
        Define a domino's head as the left one if it is horizontal
        or the upper one if it is vertical.
        2. If it is a horizontal domino, the head can be placed at (x,y)
        where x=0,1,2,3,4,5; y=0,1,2,3,4.
        If it is a vertical domino, the head can be placed at (y,x)
        where x=0,1,2,3,4,5; y=0,1,2,3,4
        3. Each integer n, between 0 and 59, represent a different placement
        of domino on the board. Every placement has three features:
        t = n mod 2;  (1 means horizontal and 0 means vertical)
        x = (n // 2) mod 6 - 1;
        y = (n // 2) // 6 - 1.
        4. Every time we select a number n (place a domino), some places can
        no longer be used.
        '''
        try:
            self._n = random.choice(self._choice)
        except IndexError:
            # n has been depleted, no possible choice to place a domino
            return False
        self._t = self._n % 2
        self._x = (self._n // 2) % 6
        self._y = (self._n // 2) // 6

        if self._t:
            # Horizontal
            self.paint(self._x,self._y,self._x,self._y+1)
        else:
            # Vertical
            self.paint(self._y,self._x,self._y+1,self._x)
        '''
        print('nxty',self._n,self._t,self._x,self._y)
        print('choice',self._choice,len(self._choice))
        self.display()
        '''
        return True

    def gameover(self):
        return len(self._choice) == 0

def main():
    count = 0
    for i in range(10000):
        b = Board()
        while b.random_paint():
            pass
        if b.dominos() == 18:
            count += 1
    print('The chance that we can paint all the squares is',count/10000)

def game():
    b = Board()
    for i in range(2):
        b.random_paint()
    print('')
    print('Game: try and fill this board with dominos')
    b.display()
    while not b.gameover():
        print('Type HELP for help. Type q to quit.')
        entry = input('Enter four numbers to place a domino at(x1,y1),(x2,y2):').strip()
        if entry.lower() == 'help':
            print('Enter four numbers within the range 1-6, representing\
                  the indices of two squares on the board. The first two\
                  numbers are the row and column of one square, the last\
                  two numbers should be the row and column of a second\
                  square. For instance, to place a horizontal domino\
                  in the upperleft corner, you would enter 1112.\n')
        elif entry.lower() == 'q':
            break
        try:
            x1 = int(entry[0]) - 1
            y1 = int(entry[1]) - 1
            x2 = int(entry[2]) - 1
            y2 = int(entry[3]) - 1
            b.paint(x1,y1,x2,y2)
            b.display()
        except:
            print('Invalid entry. Type \'HELP\' for help')
    if b.dominos() == 18:
        print('You win!')
    else:
        print('Game over')

main()
game()

############################################################################
# Test code
############################################################################


############################################################################
# This code should be uncommented and run
# after you write __init__ and .dominos()
############################################################################

# b = Board()
# print(b.dominos(), " (should print 0)")

############################################################################
# This code should be uncommented and run
# after you write .display()
############################################################################

# print("You should see an empty grid below: ")
# b.display()

############################################################################
# This code should be uncommented and run
# after you write .eligible()
############################################################################

# print(b.eligible(4,2), " (b.eligible(4,2) should be TRUE)")
# print(b.eligible(5,0), " (b.eligible(5,0) should be TRUE)")
# print(b.eligible(-1,4), " (b.eligible(-1,4) should be FALSE)")
# print(b.eligible(3,6), " (b.eligible(3,6) should be FALSE)")

############################################################################
# This code should be uncommented and run
# after you write .paint()
############################################################################

# move_one = b.paint(2, 4, 3, 4)
# print(move_one, " (move_one should be TRUE)")
# b.display()
#
# print(b.eligible(2,4), " (b.eligible(2,4) should now be FALSE)")
#
# move_two = b.paint(5, 0, 5, 1)
# print(move_two, " (move_two should be TRUE)")
# b.display()
#
# move_three = b.paint(4, 0, 5, 0)
# print(move_three, " (move_three should be FALSE)")
# b.display()
#
# move_four = b.paint(-1, 5, 0, 5)
# print(move_four, " (move_four should be FALSE)")
# b.display()

############################################################################
# This code should be uncommented and run
# after you write .random_paint()
############################################################################

# b.random_paint()
# b.random_paint()
# b.random_paint()
# print("You should see exactly 10 occupied squares below:")
# b.display()
