# Problem Set 2, hangman.py
# Name: Mehul Vikas Joshi 
# Collaborators: N/A
# Time spent: 1 week

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
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
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
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for s in secret_word:
        if s not in letters_guessed:
            return False;
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    str=""
    for s in secret_word:
        if s not in letters_guessed:
            str+= '_'
        else:
            str+=s;

    return str;

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

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
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''

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

    if guesses_left == 0:
        print("Sorry you have lost :(. Please try again later!")
        print("The word was " + secret_word)
    else:
        print("Congratulations, you won!!!")
        print("Your total score for this game is: ", guesses_left*count_unique(secret_word, letters_guessed))

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
