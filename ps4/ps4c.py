# Problem Set 4C
# Name: Mehul Joshi
# Collaborators: N/A
# Time Spent: 2hrs

import string
from ps4a import get_permutations


def load_words(file_name):
    print("Loading word list from file...")
    inFile = open(file_name, 'r')
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list



WORDLIST_FILENAME = 'words.txt'

VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words[:]

    def build_transpose_dict(self, vowels_permutation):
        transpose_dict = {}
        for l in CONSONANTS_LOWER:
            transpose_dict[l] = l
        for l in CONSONANTS_UPPER:
            transpose_dict[l] = l
        i = 0
        for v in VOWELS_LOWER:
            transpose_dict[v] = vowels_permutation[i]
            i += 1
        i = 0
        for V in VOWELS_UPPER:
            transpose_dict[V] = vowels_permutation[i].upper()
            i += 1 
        
        return transpose_dict

    def apply_transpose(self, transpose_dict):
        shift = ""
        for letter in self.message_text:
            if letter not in " !@#$%^&*()-_+={}[]|\:;'<>?,./\"":
                shift += transpose_dict[letter]
            else:
                shift += letter
        return shift

        
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        word_count = {}
        permutations = get_permutations("aeiou")
        for perm in permutations:
            word_count[perm] = 0
            words = SubMessage.apply_transpose(self, SubMessage.build_transpose_dict(self, perm)).split(" ")
           
            for w in words:
                if is_word(self.valid_words, w):
                    word_count[perm] = word_count[perm] + 1
        m = [k for k, v in word_count.items() if v == max(word_count.values())]
        return SubMessage.apply_transpose(self, SubMessage.build_transpose_dict(self, m[0]))

if __name__ == '__main__':
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    