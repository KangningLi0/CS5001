"""
    Kangning Li
    CS 5001 Spring 2024
    remix_master.py
"""

import music
import re

PUNCTUATION = ['.', ',', ':', '!', '?']

def substitute(song: list, old_word: str, new_word: str) -> bool:
    """
    Function -- substitute
        substitute every old_word with new word, while the old_word
        should be a identity not a string inside other word
        if success then remove all the punctuation
    Parameters:
        song -- the list of strings, will be modified
        old_word -- the word need to be replaced
        new_word -- the new word that replace the old word
    Return a boolean, if there exists valid old word inside the song,
        then return true, if not return false
    """
    found = False

    for i in range(len(song)):
        if old_word in song[i]:
            song[i] = replace_word(song[i], old_word, new_word)
            found = True
        
        if found:
            remove_punc(song)
    
    return found

def replace_word(sentence: str, old_word: str, new_word: str) -> str:
    """
    Function -- replace_word
        Replace a word with a new word inside a string,
        while the word need to be an entire word with spaces around
    Parameters:
        sentence -- target string to be modified
        old_word -- old word need to be replaced
        new_word -- the word that replace the old word
    Return a string that have been modified
    """
    words = split_sentence(sentence)
    
    for i in range(len(words)):
        if (i == 0 and words[i] == old_word and words[i + 1] == ' '):
            words[i] = new_word
        elif (i == len(words) - 1 and words[i] == old_word 
              and words[i - 1] == ' '):
            words[i] = new_word
        elif (i > 0 and i < len(words) - 1 and words[i] == old_word):
            if (words[i - 1] == ' ' and words[i + 1] == ' '):
                words[i] = new_word
    
    result = ''
    for word in words:
        result += word
    
    return result

def split_sentence(sentence: str) -> list:
    """
    Function -- split_sentence
        split a string into a list contains entire words and spaces
    Parameters:
        sentence -- the string that need to be modified
    Returns a list of strings and spaces, the strings should be words
    """
    pattern = r'(\s+|\b)'
    result = re.split(pattern, sentence)
    result = [token for token in result if token]

    return result

def reverse_it(song: list) -> list:
    """
    Function -- reverse_it
        split the list of strings into words
        for each string in list reverse word sequence
        and then remove all of the punctuations
    Parameters:
        song -- list of strings for sentences
    Return a list of string which have been modified
    """
    for i in range(len(song)):
        word_list = song[i].split()
        word_list.reverse()
        song[i] = " ".join(word_list)

    remove_punc(song)

    return song

def remove_punc(song: list) -> list:
    """
    Function -- remove_punc
        This function can remove every punctuation inside a song
    Parameters:
        song -- the list of strings, will be modified
    Return a list of string represent the song have been modified
        the result should not containing any punctuations
    """
    for i in range(len(song)):
        for punc in PUNCTUATION:
            song[i] = song[i].replace(punc, '')

def load_song(selection: int) -> list:
    """
    Function -- normalize
        this function take a integer represents the user's choice
        and return the song in index[0] the title in the index[1]
        if the selection is not valid, it will return empty list
    Parameters:
        selection -- represents the user's choice
    Return a list of string which is the song, if the input
        is not valid then return empty list
    """
    if (selection not in range(1, len(music.SONGS) + 1)):
        return []
    
    output_list = []

    selection_idx = selection - 1
    output_list.append(music.SONGS[selection_idx].copy())
    output_list.append(music.PLAYLIST[selection_idx])
    
    return output_list

def ui_master() -> str:
    """
    Function -- ui_master
        This function print the questions for the user
        and return the output of choice of 
        capitalized letter if the input is not valid
        return "F" letter
    Return a string containing a single letter
        which is capitalized, if the input of user is not
        valid return "F"
    """
    print("ReMix-Master:")
    print(" L: Load a different song")
    print(" T: Title of the current song")
    print(" S: Substitute a word")
    print(" P: Playback your song")
    print(" R: Reverse it!")
    print(" X: Reset to original song")
    print(" Q: Quit?")

    user_input = input("Your choice: ")
    valid_input = ["L", "l", "T", "t", "S", "s", "P", "p",
                   "R", "r", "X", "x", "Q", "q"]
    
    if user_input not in valid_input:
        return "F"
    else:
        return user_input.upper()
        
def initial_master():
    """
    Function -- initial_master
        print the first UI texts whether the user
        start the program for initial state
    """
    print("Welcome to ReMix-Master. You can remix the greatest hits!")
    print("Turn up the 808's and drop the beat! Here's your remix:")
    for sentence in music.SONGS[0]:
        print(sentence)
    print("---------------------------------------------------------")
    print("")

def main():
    """
    Function -- main
        The main function containing the entire logic
        of the remix_master
    """
    # load the first song, current_idx is for reloading
    current_song = load_song(1)
    current_idx = 0

    initial_master()

    while True:
        # Call the function to fetch the user input
        user_input = ui_master()

        if user_input == "F":
            # if user input the invalid option
            print("That is not a option. Please try again")

            # continue to next loop
            print("")
            continue

        elif user_input == "L":
            # UI shows which choice for user to take
            print("Choose the number for the song you want to load")
            for i in range(len(music.SONGS)):
                print(f"{i + 1}. {music.PLAYLIST[i]}")
            
            # Get the valid input and load the song
            second_input = input("Your choice: ")
            if second_input.isdigit():
                second_input = int(second_input)
                # change current song according to the input
                if second_input > 0 and second_input <= len(music.SONGS):
                    current_song = load_song(second_input)

                    # current_idx is used to reload a song
                    current_idx = second_input - 1
                else:
                    print("That is not a option. Please try again")
            else:
                print("That is not a option. Please try again")
            
            # continue to next loop
            print("")
            continue

        elif user_input == "T":
            # UI shows the current song title
            print("The current song title is: " + current_song[1])

            # continue to next loop
            print("")
            continue

        elif user_input == "S":
            # UI prompts the user to input the word want to replace
            old_word = input("What word do you want to "
                             "replace in the existing song? ")
            new_word = input("What new word do you want to use for the song? ")

            # the algorithm for word replacement
            if not substitute(current_song[0], old_word, new_word):
                print(f"Sorry, could not find {old_word} in the current song")

            # continue to next loop
            print("")
            continue

        elif user_input == "P":
            # Display all the sentences in current song
            for sentence in current_song[0]:
                print(sentence)

            # continue to next loop
            print("")
            continue

        elif user_input == "R":
            # reverse the current song
            reverse_it(current_song[0])

            # continue to next loop
            print("")
            continue

        elif user_input == "X":
            # reset to the original song
            current_song[0] = music.SONGS[current_idx]

            # continue to next loop
            print("")
            continue

        elif user_input == "Q":
            # quit the game and share the reward
            print("Bravo! Your Grammy Award is being shipped to you now!")

            break

if __name__ == "__main__":
    main()
    