


test_board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

#from IPython.display import clear_output


def display_board(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])


def player_input(ch):

    if (ch % 2 != 0):
        m = input("Select your marker between X or O player 1: ")
    else:
        m = input("Select your marker either X or O player 2: ")
    m = m.upper()
    if ((m == 'X') or (m == 'O')):
        return m
    while ((m != 'X') or (m != 'O')):
        m = input("Select your marker again: ")
        m = m.upper()
        if ((m == 'X') or (m == 'O')):
            break

    return m

def place_marker(board, marker, position):
    board[position] = marker
    return board


def win_check(board, mark):
    if (board[1] == board[2] == board[3] == mark):
        print(f"Player with {mark} won!!")
        return 'OFF'

    elif (board[4] == board[5] == board[6] == mark):
        print(f"Player with {mark} won!!")
        return 'OFF'

    elif (board[7] == board[8] == board[9] == mark):
        print(f"Player with {mark} won!!")
        return 'OFF'

    elif (board[1] == board[5] == board[9] == mark):
        print(f"Player with {mark} won!!")
        return 'OFF'

    elif (board[3] == board[5] == board[7] == mark):
        print(f"Player with {mark} won!!")
        return 'OFF'

    elif (board[1] == board[4] == board[7] == mark):
        print(f"Player with {mark} won!!")
        return 'OFF'

    elif (board[3] == board[6] == board[9] == mark):
        print(f"Player with {mark} won!!")
        return 'OFF'

    elif (board[2] == board[5] == board[8] == mark):
        print(f"Player with {mark} won!!")
        return 'OFF'


import random
from random import randint

def choose_first():
    r=randint(1,2)
    print (f"The first move is of player:  {str(r)}")
    return (int(r))


def full_board_check(board):
    x=1
    while(x<10):
        if (board[x] == ' '):
            return False
            break
        x=x+1
        if (x==10):
            return True


def player_choice():
    x=True

    while (x==True):


        n = input("Enter your next position Player: ")


        if (int(n) >= 10):
            print("Invalid position!! Please enter between 1 to 9")
            continue
        else:
            x = False

    return (int(n))


def space_check(board, position):
    add = True

    if (board[position] == " "):
        return True
    else:
        print("Position not empty")
        add = False


def replay():
    n= input ("You want to play again, Yes or No?: ")
    if (n=="Yes"):
        return True
    else:
        return False


play = True

while (play == True):
    test_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    print('Welcome to Tic Tac Toe!')
    display_board(test_board)                                # Displaying the empty board

    r1 = choose_first()                                      # Randomly choosing 1st player

    mark = player_input(r1)                                  # Taking marker from player until he gives correct entry
    game = 'ON'
    full = False

    while (game == 'ON'):                                     # Starting the game loop

        pos = player_choice()                                  # Returning the player choice of position

        place = space_check(test_board, pos)                   # Checking if the position is empty

        if (place == True):

            newtest_board = place_marker(test_board, mark,pos)     # Assigning the marker to the position and calling display function

            display_board(newtest_board)

            w = win_check(newtest_board, mark)                     # Checking if someone won

            if (w == 'OFF'):
                game = 'OFF'
                break

            full = full_board_check(newtest_board)                # checking if the board is full or not

            if (full == True):                                     # out of game loop once board is full
                print("Its a Toss")
                game = 'OFF'
                break
            test_board = newtest_board
            if mark == 'X':
                mark = 'O'
            else:
                mark = 'X'

    if (game == 'OFF'):
        r=replay()
    if (r== True):
        game = 'ON'
        play = True

    else:
        play = False
        break
