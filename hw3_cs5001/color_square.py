"""
Kangning Li
CS 5001 Spring 2024
color_square.py
"""


def black_or_white(row, column):
    # print the color of the location of the chessboard
    column_num = ord(column.lower()) - 96

    # if the row input is string change it into integer
    if (int(row) + column_num) % 2 == 1:
        return "WHITE"
    else:
        return "BLACK"


          
