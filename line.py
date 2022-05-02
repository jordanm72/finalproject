from word import Word
# this class ended up being redundant, so for the final report, it is not called or used at all. I just kept it in case
# it would be useful in the future

class Line:
    """Class for a line of words, some of which may be misspelled"""
    def __init__(self, line, dict):
        # creates line object using the string of the line and dictionary of correct words
        self.line = line
        self.dict = dict

    def __str__(self):
        return self.line

    def checkLine(self):
        """for each word in the line, checks and fixes it
        :param: No parameters
        :return: list of tuples containing the original word and the corrected word
        """
        corrected = []
        # for each word in the line, checks if it is misspelled. If so, fixes the word using the checkSpelled function
        for word in self.line.split(" "):
            w = Word(word, self.dict, self.line)
            if not w.checkSpelled():
                corrected.append([word, w.checkWord()])
        # returns a list of corrected words and the originals
        return corrected

