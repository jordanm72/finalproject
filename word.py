from itertools import permutations


class Word:
    """Class to represent a misspelled word and functions to correct it"""
    def __init__(self, word, dict, line):
        self.word = word
        self.dict = dict
        self.line = line

    def __str__(self):
        """Overloads the string operator to return a string containing just the word"""
        return self.word

    def checkWord(self):
        """Finds alternatives to the misspelled word, has the user pick which alternative they want, and returns a tuple
        containing the original word and the replacement word
        :param: No parameters
        :return: A tuple containing the original word and the replacement word
        """
        # gets a list of possible intended words
        ist = self.findAlternatives()
        # sorts the list by the arbitrary designations of how similar they are to the original
        ist = sorted(ist, key=lambda x: x[1])
        # returns the word chosen by the user to correct the misspelled word
        return self.chooseAlternative(ist, self.line)

    def checkSpelled(self):
        """checks if the word is in the dictionary
        :param: No parameters
        :return: True if in dictionary, False otherwise
        """
        if self.word in self.dict:
            return True
        return False

    def findAlternatives(self):
        """for the misspelled word, calls 6 helper methods to find similar words, and returns a list of all the unique
        similar words
        :param: No parameters
        :return: A list containing tuples with unique similar words and a number corresponding to their likelihood
        """
        answer = []
        checkreplicates = []
        # calls all of the supporting functions to find intended words and stores them in a list
        # for each word, makes sure it is not a duplicate of an already found intended word
        for ans in self.removeDouble():
            if ans[0] not in checkreplicates:
                answer.append(ans)
                checkreplicates.append(ans[0])
        for ans in self.singleTranspositions():
            if ans[0] not in checkreplicates:
                answer.append(ans)
                checkreplicates.append(ans[0])
        for ans in self.addDouble():
            if ans[0] not in checkreplicates:
                answer.append(ans)
                checkreplicates.append(ans[0])
        for ans in self.permutations():
            if ans[0] not in checkreplicates:
                answer.append(ans)
                checkreplicates.append(ans[0])
        for ans in self.vowelPermutations():
            if ans[0] not in checkreplicates:
                answer.append(ans)
                checkreplicates.append(ans[0])
        for ans in self.transpose():
            if ans[0] not in checkreplicates:
                answer.append(ans)
                checkreplicates.append(ans[0])
        return answer

    def chooseAlternative(self, ist, line):
        """gives the user a list of possible words, and has them choose a word. Returns a tuple of the word they choose
        and a number indicating its similarity to the original
        :param ist: a List containing the similar words
        :param line: a string with the line of the misspelled word
        :return: A tuple containing the chosen intended word and its similarity number
        """
        # prints the incorrectly spelled word, its line, and the first 20 suggested words (or as many exist)
        print("\n The incorrectly spelled word is: " + str(self.word) + "\nIt's line is: ")
        print(self.line)
        print("Here is a list of possible intended words, along with an index showing how close they are to the"
              " original. Lower is closer to the original")
        for i in range(min(20, len(ist))):
            print("Index = " + str(i) + str(ist[i]))
        # user chooses which word, chooses to enter a custom word, or chooses not to replace the word
        sentence = ("Enter the index of the word you want to replace the misspelled one. If you don't want to replace "
                    "the word, enter -1. Enter -2 if you want to replace with a custom word")
        i = int(input(sentence))
        if i == -1:
            return (self.word, 0)
        if i == -2:
            return (input("Enter the word you want"), 0)
        # lets the user choose to capitalize a word if necessary
        if 0 <= i <= min(20, len(ist)):
            upper = int(input("If you want the first letter to be capitalized, enter 1"))
            if upper == 1:
                return (ist[i][0].capitalize(), ist[i][1])
        # returns the user's chosen word
        if i < min(20, len(ist)):
            return ist[i]
        return (self.word, 0)

    def singleTranspositions(self):
        """creates possible words by flipping pairs of letters. Ex: turns "wrogn" into "wrong"
        :param: No parameters
        :return: A list containing tuples with similar words and the number 2 (which corresponds to their likelihood)
        """
        # creates possible words by flipping pairs of letters. Example: turns "wrogn" into "wrong"
        answer = []
        w = self.word
        # for each pair of letters
        for i in range(len(w) - 1):
            new = w[:i] + (w[i + 1] + (w[i] + (w[i + 2:])))
            # checks if new word is a word
            if new in self.dict:
                answer.append((new, 2))
        return answer

    def permutations(self):
        """creates possible words by considering permutations of the word if the word is less than 6 letters
        :param: No parameters
        :return: A list containing tuples with correctly spelled permutations of the word and the number 6
        (which corresponds to their likelihood as the intended word)
        """
        # for words less than 6 letters, considers
        # permutations of the word. Ex: turns "ritgh" to "right"
        answer = []
        if len(self.word) < 6:
            # uses permutations function from itertools
            for l in permutations(self.word):
                answer.append("".join(l))
        words = []
        for ans in answer:
            if ans in self.dict:
                words.append((ans, 6))
        return words

    def vowelPermutations(self):
        """creates possible words by considers permutations of the vowels in the word.
        Ex: turns "understindang" to "understanding"
        :param: No parameters
        :return: A list containing tuples with the permutations and the number 4 (which corresponds to their likelihood)
        """
        # considers permutations of the vowels in a word. Ex: turns "understindang" to "understanding"
        vowels = ""
        indices = []
        # stores all of the vowels and their indices
        for i in range(len(self.word)):
            if self.word[i] in ["a", "e", "i", "u", "o"]:
                vowels = vowels + self.word[i]
                indices.append(i)
        answers = []
        # finds permutations of the vowels. For each permutation, creates the new word using the new combination of
        # vowels.
        for perm in permutations(vowels):
            # new word is the same as the old word up until the first vowel
            new = self.word[:indices[0]] + perm[0]
            # for each vowel, fills in the consonants up until the vowel, and then adds the vowel
            for j in range(1, len(vowels)):
                new = new + self.word[indices[j - 1] + 1:indices[j]] + perm[j]
            # adds the remaining consonants to the end
            new = new + self.word[indices[len(vowels) - 1] + 1:]
            if new in self.dict:
                answers.append((new, 4))
        return answers

    def addDouble(self):
        """creates possible words by replacing single letters with double letters. Ex: "turns sucess" to "success"
        :param: No parameters
        :return: A list containing tuples with the new words and the number 3 (corresponds to their likelihood)
        """
        answer = []
        w = self.word
        # for each letter in the word
        for i in range(len(w)):
            # creates a new by adding the same letter next to itself to create a double letter
            new = w[:i] + w[i] + w[i:]
            if new in self.dict:
                answer.append((new, 3))
        return answer

    def removeDouble(self):
        """creates possible words by removing double letters. Ex: turns "worrds" to "words"
        :param: No parameters
        :return: A list containing tuples with the new words and the number 1 (which corresponds to their likelihood)
        """
        answer = []
        w = self.word
        for i in range(0, len(w) - 1):
            if w[i + 1] == w[i]:
                new = w
                new = new[:i] + new[i + 1:]
                if new in self.dict:
                    answer.append((new, 1))
        return answer

    def transpose(self):
        """creates possible words by replacing letters with other letters in the alphabet.
        Ex: turns "misteke" to "mistake"
        :param: No parameters
        :return: A list containing tuples with the new words and the number 5 (which corresponds to their likelihood)
        """
        answer = []
        w = self.word
        letters = "abcdefghijklmnopqrstuvwxyz"
        # for each letter in the word
        for i in range(len(w) - 1):
            # for each letter in the alphabet
            for j in range(26):
                # creates a new word that replaces the original letter by a different letter in the alphabet
                new = w[:i] + letters[j] + w[(i + 1):]
                new = new.strip("\n")
                if new in self.dict:
                    answer.append((new, 5))
        return answer

