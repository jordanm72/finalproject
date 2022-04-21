from word import Word


class Line:

    def __init__(self, line, dict):
        self.line = line
        self.dict = dict

    def __str__(self):
        return self.line

    def checkLine(self):
        corrected = []
        for word in self.line.split(" "):
            w = Word(word, self.dict, self.line)
            if not w.checkSpelled():
                corrected.append([word, w.checkWord()])
        return corrected

