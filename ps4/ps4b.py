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
        s = ""
        for w in self.message_text:
            s += w
        return s


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
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        pass #delete this line and replace with your code here

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        pass #delete this line and replace with your code here

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        pass #delete this line and replace with your code here

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        pass #delete this line and replace with your code here

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        pass #delete this line and replace with your code here


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        pass #delete this line and replace with your code here

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        pass #delete this line and replace with your code here

if __name__ == '__main__':
    message = Message("hello world")
    print(message.get_message_text())
    message.apply_shift(2)
#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE

    #TODO: best shift value and unencrypted story 
    
    pass #delete this line and replace with your code here
