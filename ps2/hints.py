# Problem Set 2, hangman.py
# Name: Mehul Vikas Joshi 
# Collaborators: N/A
# Time spent: 2 hrs

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    return random.choice(wordlist)

# end of helper code
# -----------------------------------
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    for s in secret_word:
        if s not in letters_guessed:
            return False;
    return True


def get_guessed_word(secret_word, letters_guessed):
    str=""
    for s in secret_word:
        if s not in letters_guessed:
            str+= '_'
        else:
            str+=s;

    return str;

def get_available_letters(letters_guessed):
    letters = string.ascii_lowercase
    remaining_letters = ''
    for letter in letters:
        if letter not in letters_guessed:
            remaining_letters += letter
    return remaining_letters


def count_unique(secret_word, letters_guessed):
    unique = 0
    for letter in letters_guessed:
        if letter in secret_word:
            unique += 1
    return unique


def hangman(secret_word):
    print("Welcome to the game Hangman!")
    print('I am thinking of a word that is ' + str(len(secret_word)) + " letters long.")
    guesses_left = 6
    warnings_left = 3
    print("You have 3 warnings left")
    letters_guessed = [];
    while guesses_left > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("You have " + str(guesses_left) + " guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        letter = input("Please guess a letter: ")
        if letter in letters_guessed:
            print("Oops! You've already guessed that letter.", end='')
            if warnings_left > 0:
                warnings_left -= 1
            else:
                guesses_left -= 1
            print("You have " + str(warnings_left) + " warnings left: ", get_guessed_word(secret_word,letters_guessed))

        elif letter not in string.ascii_lowercase:
            print("Oops! That is not a vaild letter.", end="")
            if warnings_left > 0:
                warnings_left -= 1
            else:
                guesses_left -= 1
            print(" You have " + str(warnings_left) + " warnings left: ", get_guessed_word(secret_word,letters_guessed))

        elif letter not in secret_word:
            letters_guessed.append(letter)
            print("Oops! That letter is not in my word: ", get_guessed_word(secret_word,letters_guessed))
            if letter in "aeiouy":
                guesses_left -= 2
            else:
                guesses_left -= 1

        else:
            letters_guessed.append(letter)
            print("Good guess: ", get_guessed_word(secret_word,letters_guessed))
        print("-------------------------------------------")

    if guesses_left <= 0:
        print("Sorry you have lost :(. Please try again later!")
        print("The word was " + secret_word)
    else:
        print("Congratulations, you won!!!")
        print("Your total score for this game is: ", guesses_left*count_unique(secret_word, letters_guessed))

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


def match_with_gaps(my_word, other_word):
    if len(my_word) == len(other_word):
        for i in range(0, len(my_word)):
            if my_word[i] != '_' and my_word[i] != other_word[i]:
                return False 
        return True
    else:
        return False 



def show_possible_matches(my_word):
    for word in wordlist:
        if len(word) == len(my_word):
            if match_with_gaps(my_word, word):
                print(" "+word, end='')


def hangman_with_hints(secret_word):
    print("Welcome to the game Hangman!")
    print('I am thinking of a word that is ' + str(len(secret_word)) + " letters long.")
    guesses_left = 6
    warnings_left = 3
    print("You have 3 warnings left")
    letters_guessed = [];
    while guesses_left > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("You have " + str(guesses_left) + " guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        letter = input("Please guess a letter: ")
        if letter == "*":
            print("Possible matches are:", end="") 
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        elif letter in letters_guessed:
            print("Oops! You've already guessed that letter.", end='')
            if warnings_left > 0:
                warnings_left -= 1
            else:
                guesses_left -= 1
            print("You have " + str(warnings_left) + " warnings left: ", get_guessed_word(secret_word,letters_guessed))
        elif letter not in string.ascii_lowercase:
            print("Oops! That is not a vaild letter.", end="")
            if warnings_left > 0:
                warnings_left -= 1
            else:
                guesses_left -= 1
            print(" You have " + str(warnings_left) + " warnings left: ", get_guessed_word(secret_word,letters_guessed))

        elif letter not in secret_word:
            letters_guessed.append(letter)
            print("Oops! That letter is not in my word: ", get_guessed_word(secret_word,letters_guessed))
            if letter in "aeiouy":
                guesses_left -= 2
            else:
                guesses_left -= 1

        else:
            letters_guessed.append(letter)
            print("Good guess: ", get_guessed_word(secret_word,letters_guessed))
        print("-------------------------------------------")

    if guesses_left <= 0:
        print("Sorry you have lost :(. Please try again later!")
        print("The word was " + secret_word)
    else:
        print("Congratulations, you won!!!")
        print("Your total score for this game is: ", guesses_left*count_unique(secret_word, letters_guessed))


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


# -----------------------------------

if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
