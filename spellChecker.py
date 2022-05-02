from line import Line
from word import Word
import string


class SpellChecker:
    """Spell checker class for storing lists of text from a file and running spell checks on them"""
    def __init__(self):
        ist = []
        name = input("Enter the name of the text file you want to correct")
        self._name = name
        # opens text file, replaces punctuation and excess spaces, and reads line by line into a list
        with open(self._name) as f:
            for line in f:
                line1 = line
                s = string.punctuation
                s.replace("'", "")
                for letter in line1:
                    if letter in s:
                        line1 = line1.replace(letter, "")
                line1 = line1.strip("\n")
                line1 = line1.strip(" ")
                lower = line1.lower()
                ist.append(lower)
        self._lines = ist
        # reads entire text file into a string
        with open(self._name) as f:
            self._text = f.read()
        words = {}
        # opens a dictionary text file, and stores each word in a dictionary
        with open('words_alpha.txt') as w:
            for w in w.read().split("\n"):
                words[w] = ""
        self._dict = words
        self._corrected = []

    def check(self):
        """iterates over each word in each line, finds a corrected word if necessary, and then replaces each word
        in the original text and overwrites the original file
        :param: No parameters
        :return: None
        """
        # creates a line object for each line, and calls the function to check the line
        for line in self._lines:
            corrected = []
            for word in line.split(" "):
                w = Word(word, self._dict, line)
                if not w.checkSpelled():
                    corrected.append([word, w.checkWord()])
            self._corrected.append(corrected)
        # calls two supporting function to replace misspelled words and overwrite original text file
        self.replace()
        self.write()
        print("Successfully replaced any misspelled words in the original text file")

    def replace(self):
        """for each misspelled word and its corrected word, replaces the misspelled word by its correction in the
        string holding the original text
        :param: No parameters
        :return: None
        """
        for instance in self._corrected:
            for word in instance:
                # if the replacement word is not the same as the original word
                if word[0] != word[1][0]:
                    self._text = self._text.replace(word[0], word[1][0])
                    # accounts for capitalization since I turned the original text lowercase in self._lines
                    self._text = self._text.replace(word[0].capitalize(), word[1][0])

    def write(self):
        """overwrites original text file with corrected string
        :param: No parameters
        :return: None
        """
        with open(self._name, 'w') as f:
            f.write(self._text)








