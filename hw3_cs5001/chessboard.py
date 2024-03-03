"""
Kangning Li
CS 5001 Spring 2024
chessboard.py
"""

def check_valid_row(row):
    # check if the number is integer and within the range
    if isinstance(row, int):
        if row < 1 or row > 8:
            return False
        else:
            return True
    elif isinstance(row, str):
        # if the input is string change it into integer
        if int(row) >= 1 and int(row) <= 8:
            return True
        else:
            return False
    else:
        return False

def check_valid_column(column):
    # check the input is the single letter within range
    if len(column) == 1 and isinstance(column, str):
        if ord(column.lower()) < 97 or ord(column.lower()) > 104:
            return False
        else:
            return True
    else:
        return False



    
