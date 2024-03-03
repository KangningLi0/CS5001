"""
Kangning Li
CS 5001 Spring 2024
test_square.py
"""

def check_valid_row(row):
    # the test function 1
    if isinstance(row, str):
        if int(row) < 1 or int(row) > 8:
            return False
        else:
            return True
    
    if isinstance(row, int):
        if row < 1 or row > 8:
            return False
        else:
            return True

    return False

def check_valid_column(column):
    # the test function 2
    if len(column) == 1 and isinstance(column, str):
        if (ord(column.lower()) < 97 or ord(column.lower()) > 104):
            return False
        else:
            return True
    else:
        return False

def test_squares():
    # using simple logic to complete the test path
    column_test_1 = check_valid_column("i")
    column_test_2 = check_valid_column("A")
    column_test_3 = check_valid_column("B")

    print(f"Column: i, Expected: False, Actual: {column_test_1}")
    print(f"Column: A, Expected: False, Actual: {column_test_2}")
    print(f"Column: B, Expected: False, Actual: {column_test_3}")

    row_test_1 = check_valid_row(1)
    row_test_2 = check_valid_row(2)
    row_test_3 = check_valid_row(3)

    print(f"Row: 1, Expected: True, Actual: {row_test_1}")
    print(f"Row: 2, Expected: True, Actual: {row_test_1}")
    print(f"Row: 3, Expected: True, Actual: {row_test_1}")
    
    
