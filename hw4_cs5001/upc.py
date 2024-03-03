"""
Kanging Li
CS 5001 Spring 2024
upc.py
"""

def is_valid_upc(list_of_integers: list) -> bool:
    """
    this function determines whether a given list
    of integers represents a valid UPC
    """
    if len(list_of_integers) < 2:
        return False

    # value to store the sum
    det = 0
    oddPos = False

    # actual algorithm form the sum
    while len(list_of_integers) > 0:
        if oddPos:
            det += 3 * list_of_integers.pop()
            oddPos = False
        else:
            det += list_of_integers.pop()
            oddPos = True

    # the code to forbid the wrong case
    if det == 0:
        return False
    elif det % 10 != 0:
        return False
    else:
        return True


def main():
    # Test Code
    print(is_valid_upc([0, 7, 3, 8, 5,
                        4, 0, 0, 8, 0,
                        8, 9]))

if __name__ == "__main__":
    main()
