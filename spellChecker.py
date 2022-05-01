from line import Line
from word import Word
import string


class SpellChecker:
    """Spell checker class"""
    def __init__(self):
        ist = []
        name = input("Enter the name of the text file you want to correct")
        self.name = name
        # opens text file, replaces punctuation and excess spaces, and reads line by line into a list
        with open(self.name) as f:
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
        self.lines = ist
        # reads entire text file into a string
        with open(self.name) as f:
            self.text = f.read()
        words = {}
        # opens a dictionary text file, and stores each word in a dictionary
        with open('words_alpha.txt') as w:
            for w in w.read().split("\n"):
                words[w] = ""
        self.dict = words
        self.corrected = []

    def check(self):
        # creates a line object for each line, and calls the function to check the line
        for line in self.lines:
            #l = Line(line, self.dict)
            corrected = []
            for word in line.split(" "):
                w = Word(word, self.dict, line)
                if not w.checkSpelled():
                    corrected.append([word, w.checkWord()])
            self.corrected.append(corrected)
        # calls two supporting function to replace misspelled words and overwrite original text file
        self.replace()
        self.write()
        print("Successfully replaced any misspelled words in the original text file")

    def replace(self):
        # for each misspelled word and its corrected word, replaces the misspelled word by its correction in the
        # string holding the original text. Also accounts for capitalized words
        for instance in self.corrected:
            for word in instance:
                if word[0] != word[1][0]:
                    self.text = self.text.replace(word[0], word[1][0])
                    self.text = self.text.replace(word[0].capitalize(), word[1][0])

    def write(self):
        # overwrites original text file with corrected string
        with open(self.name, 'w') as f:
            f.write(self.text)



s = SpellChecker()
s.check()






