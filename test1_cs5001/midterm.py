"""
Kangning Li
CS 5001 Spring 2024
midterm.py
"""

def identify(number: int) -> str:
    """
    Function -- identify
        identify the type of credit card from the input number
    Parameter:
        number --- credit card number
    Return a string indice the type of credit card, and return "Unknown"
        for cards that cannot be identified
    """

    # Convert number into string and get the length
    number = str(number)
    card_len = len(number)

    # Deal with each cases
    if card_len == 15 and number[0] == '3':
        return "American Express"
    elif card_len == 14 and number[0] == '3':
        return "Diners Club"
    elif card_len == 16 and number[0] == '6':
        return "Discover"
    elif card_len == 16 and number[0] == '3':
        return "JCB"
    elif card_len == 16 and number[0] == '5':
        return "Mastercard"
    elif (card_len == 13 or card_len == 16) and number[0] == '4':
        return "Visa"
    else:
        return "Unknown"
    
def every_other(a_list: list[int]) -> None:
    """
    Function -- every_other
        this function take every odd-numbered index and apply *2 to that
        element, and update the index with resultant value
    Parameters:
        a_list -- the incoming list that we need to modified
    """

    a_len = len(a_list)

    # apply *2 to every odd-number element
    for i in range(a_len):
        if i % 2 == 1:
            a_list[i] *= 2

def resequencing(a_list: list) -> str:
    """
    Function -- resequencing
        this function reorder the elements in the input list and reorder
        it by ascending order and then merging it into a string
    Parameters:
        a_list -- the incoming list passed as the input
    Return a string containing the elements of the list, sorted in ascending
        order, and each separated by a space
    """

    # Copy the input list and sort the copy list
    result_list = a_list.copy()
    result_list.sort()

    # Make elements in list into string and join them by spaces
    result_list = [str(element) for element in result_list]
    result_list = " ".join(result_list)

    return result_list

def word_play(word_list: list[str], letter_1: str, letter_2: str) -> None:
    """
    Function -- word_play
        this function traverse every word, if contains letter1 convert into
        letter2, else if contain letter2 convert into letter1, if
        the word list do not have letter1 and letter2, we leave thing
        unchanged
    Parameters:
        word_list -- the list of word we need to traverse and modified
        letter_1 -- string represent the first letter
        letter_2 -- string represent the second letter
    """
    list_len = len(word_list)

    # convert main algorithm
    for i in range(list_len):
        if letter_1 in word_list[i]:
            word_list[i] = word_list[i].replace(letter_1, letter_2)
        elif letter_2 in word_list[i]:
            word_list[i] = word_list[i].replace(letter_2, letter_1)

def flipper(a_list: list[bool]) -> list[bool]:
    """
    Function -- flipper
        this function "flips" each boolearn value make true to false,
        and make false to true
    Parameters:
        a_list -- a list of boolean value
    Returns a list of boolean value that have the "flipped" side of a_list
    """
    answer_list = []

    # the main algorithm
    for value in a_list:
        if value == True:
            answer_list.append(False)
        else:
            answer_list.append(True)
    
    return answer_list
