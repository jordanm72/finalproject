from line import Line
from word import Word
import string


class SpellChecker:
    """Spell checker class"""
    def __init__(self, name):
        ist = []
        self.name = name
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
        with open(self.name) as f:
            self.text = f.read()
        words = {}
        with open('words_alpha.txt') as w:
            for w in w.read().split("\n"):
                words[w] = ""
        self.dict = words
        self.corrected = []

    def check(self):
        for line in self.lines:
            l = Line(line, self.dict)
            self.corrected.append(l.checkLine())
        self.replace()
        self.write()

    def replace(self):
        print(self.corrected)
        for instance in self.corrected:
            for word in instance:
                if word[0] != word[1][0]:
                    self.text = self.text.replace(word[0], word[1][0])
                    self.text = self.text.replace(word[0].capitalize(), word[1][0])

    def write(self):
        with open(self.name, 'w') as f:
            f.write(self.text)



s = SpellChecker("test.txt")
s.check()






