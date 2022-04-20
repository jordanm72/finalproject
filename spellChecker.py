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
                print("Got here")
                s = string.punctuation
                s.replace("'", "")
                for l in s:
                    line.replace(l, "")
                lower = line.lower()
                ist.append(lower)
            self.text = f.read()
        self.lines = ist
        words = {}
        with open('words_alpha.txt') as w:
            for line in w:
                words[line] = ""
        self.dict = words
        self.corrected = []

    def check(self):
        for line in self.lines:
            l = Line(line, self.dict)
            self.corrected.append(l.checkLine())
        self.replace()
        self.write()

    def replace(self):
        for instance in self.corrected:
            self.text.replace(instance[0], instance[1])

    def write(self):
        with open(self.name, 'w') as f:
            f.write(self.text)



s = SpellChecker("test.txt")
s.check()
print(s.lines)





