# Problem Set 4B
# Name: Mehul Joshi
# Collaborators: N/A
# Time Spent: 2hrs

import string


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

def get_story_string():
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
       self.message_text = text
       self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        dict = {}
        for i in range(0, 52):
            elem=''
            if i < 26:
                if i+shift < 26:
                     elem = chr(i+shift+65)
                else:
                    elem = chr(i+shift + 65 - 26)
                dict[chr(i+65)] = elem 
            else:

                if i+shift < 52:
                    elem = chr(i+shift+71)
                else:
                    elem =chr(i+shift+45)
                dict[chr(i+71)] = elem
        return dict

    def apply_shift(self, shift):
        dict = self.build_shift_dict(shift)
        encrypted = ""
        for s in self.message_text:
            if s not in " !@#$%^&*()-_+={}[]|\:;'<>?,./\"":
                encrypted += dict[s]
            else:
                encrypted += s
        return encrypted


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        
    def get_shift(self):
        return self.shift
    def get_encryption_dict(self):
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
       return self.message_text_encrypted

    def change_shift(self, shift):
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(shift)

class CiphertextMessage(Message):
    def __init__(self, text):
        Message.__init__(self, text)


    def decrypt_message(self):
        word_count = {}
        for i in range(0, 27):
            decrypted = self.apply_shift(i).split(" ")
            word_count[i] = 0
            for w in decrypted:
                if w in self.valid_words:
                    word_count[i] = word_count[i] + 1
        m = [k for k, v in word_count.items() if v == max(word_count.values())]
        return (m[0], self.apply_shift(m[0]))

        



if __name__ == '__main__':
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())
    
   
    