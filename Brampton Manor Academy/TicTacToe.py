from math import inf as infinity
import random
from random import choice
import platform
import time
from os import system

PLAYER = 'X'
AI = 'O'
EMPTY = ' ' 

def empty_cells(Board):
    empty = []
    for Row in Board:
        for Column in Board:
            if Board[Row][Column] == EMPTY:
                Coordinate = str(Row) + str(Column)
                empty.append(Coordinate)
    return empty

def draw_board(Board):
    for Row in Board:
        print(Row)

def player_turn(Board):
    Valid = True
    draw_board(Board)
    print()
    Coordinate = input("Enter Coordinates to place 'X': ")
    if len(Coordinate) != 2:
        Valid = False
    else:
        try:
            Row = int(Coordinate[0])
        except:
            Valid = False
        try:
            Column = int(Coordinate[1])
        except:
            Valid = False
        if (Row < 0 or Row > 2):
            Valid = False
        if (Column < 0 or Column > 2):
            Valid = False
    if not Valid:
        print("Invalid input\n")
        player_turn(Board)
    else: 
        Board[Row][Column] = PLAYER
        print()
        draw_board(Board)
    return Board

def ai_turn(Board):
    print()
    print("AI's turn: ")
    Valid = True
    Row = random.randint(0,2)
    Column = random.randint(0,2)
    if Board[Row][Column] != EMPTY:
        ai_turn(Board)
    else:
        Board[Row][Column] = AI
         
def main():
    Board = [[EMPTY for Column in range(0,3)] for Row in range(0,3)]
    Finished = False
    Turn = True
    while Finished == False:
        if Turn == True:
            player_turn(Board)
            Turn = False
        else:
            ai_turn(Board)
            Turn = True
    
        
if __name__ == '__main__':
    main()
