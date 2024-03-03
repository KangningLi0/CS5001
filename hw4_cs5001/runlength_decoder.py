"""
Kangning Li
CS 5001 Spring 2024
runlength_decoder.py
"""

import hw4data


def decode(data: list) -> list:
    """
    This function takes a list of RLE-encoded values as its single parameter
    and returns a list containing the decoded values
    """
    
    output_list = []
    
    for i in range(len(data)):
        if i % 2 == 0:
            # if idx is even it's the letter we need to output
            letter_to_add = data[i]
        elif i % 2 == 1:
            # if idx is odd it's the occurence of letter
            for i in range(data[i]):
                output_list.append(letter_to_add)

    return output_list
