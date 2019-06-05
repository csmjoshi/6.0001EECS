# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Mehul Joshi
# Collaborators : N/A
# Time spent    : 1hr

import math
import random
import string

VOWELS = 'aeiou*'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    '*':0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


def get_word_score(word, n):
    word=word.lower()
    sum = 0
    for letter in word:
        sum += SCRABBLE_LETTER_VALUES[letter]
    const = 1
    if((7*len(word) - 3*(n-len(word))) > 1):
        const = (7*len(word) - 3*(n-len(word)))
    return sum * const 
    

def display_hand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      
    print()                              

def deal_hand(n):
    hand={}
    num_vowels = int(math.ceil(n / 3))
    hand['*']=hand.get('*', 0) + 1
    for i in range(1, num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    return hand

def update_hand(hand, word):
    word = word.lower()
    new_hand = {}
    for letter in hand.keys():
            new_hand[letter] = hand[letter]
    for letter in word:
        if letter in new_hand:
            new_hand[letter] = new_hand.get(letter) - 1
    dict = {}
    for i in new_hand.keys():
        if new_hand.get(i) > 0:
            dict[i] = new_hand[i]
    return dict

def is_valid_word(word, hand, word_list):
    word=word.lower()
    new_hand = {}
    for letter in hand.keys():
            new_hand[letter] = hand[letter]
    for letter in word:
        if letter in new_hand and new_hand[letter] > 0:
            new_hand[letter] = new_hand.get(letter) - 1
        else:
            return False
    if '*' in word:
        return len(show_possible_matches(word, word_list)) > 0
    else:
        return word in word_list
    
def show_possible_matches(word, word_list):
    L = []
    for w in word_list:
        if len(word) == len(w) and match_with_gaps(word, w):
            L.append(w)
    return L
     
def match_with_gaps(word, w):
    for i in range(0, len(word)):
        if word[i] != '*' and word[i] != w[i]:
            return False
        elif word[i] == '*' and w[i] not in VOWELS:
            return False
    return True
#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    letter_count = 0
    for key in hand.keys():
       letter_count += hand[key]
    return letter_count
    
def play_hand(hand, word_list):
   
    x=""
    score=0
    while 1==1:
        print()
        print("Current hand: ", end="")
        display_hand(hand)
        x=input("Enter word, or !! to quit: ")
        
        if x == "!!":
            print("Thank you for playing.")
            break
        elif calculate_handlen(update_hand(hand, x)) == 0:
            print("Sorry you have no more letters left")
            break
        if is_valid_word(x, hand, word_list):
            score+=get_word_score(x, calculate_handlen(hand))
            print('"' + x + '" earned', get_word_score(x, calculate_handlen(hand)), 
            "points. Total:", score, "points.")
        else:
            print("That is not a valid word! Please choose another word.")
        
        hand=update_hand(hand, x)
    print("Total: ", score, " points")
    return score




#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    new_hand = {}
    for letters in hand.keys():
        if letters != letter:
            new_hand[letters] = hand[letters]
    for i in range(hand[letter]):
        if letter in VOWELS:
            x=random.choice(VOWELS)
            while x in hand.keys():
                x=random.choice(VOWELS)
            new_hand[x]=new_hand.get(x, 0) + 1
        else:
            x=random.choice(CONSONANTS)
            while(x in hand.keys()):
                x=random.choice(CONSONANTS)  
            new_hand[x] = new_hand.get(x, 0) + 1

    return new_hand

    
   
    
if __name__ == '__main__':
    play_hand(deal_hand(HAND_SIZE), load_words())