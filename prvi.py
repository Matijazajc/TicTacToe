# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:31:01 2019

@author: MatijaZajc
"""
"""
How to play the game: enter which space you want 
to put the X or 0 at (depending whos turn it is)
 available places: top-L, top-M, top-R, mid-L, mid-M, mid-R, low-L, low-M,low-R

"""
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
 print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
 print('-+-+-')
 print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
 print('-+-+-')
 print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)
turn="X"
for i in range(9):
    print("Its "+turn+" on which space")
    move=input()
    theBoard[move]=turn
    printBoard(theBoard)
    if turn=="X":
        turn="0"
    else:
        turn="X"

    
    