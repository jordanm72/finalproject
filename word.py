from itertools import permutations


class Word:
    """Class"""
    def __init__(self, word, dict, line):
        self.word = word
        self.dict = dict
        self.line = line

    def __str__(self):
        return self.word

    def checkWord(self):
        ist = self.findAlternatives()
        ist = sorted(ist, key=lambda x: x[1])
        return self.chooseAlternative(ist, self.line)

    def checkSpelled(self):
        if self.word in self.dict:
            return True
        return False

    def findAlternatives(self):
        answer = []
        checkreplicates = []
        for ans in self.removeDouble():
            if ans[0] not in checkreplicates:
                answer.append(ans)
                checkreplicates.append(ans[0])
        for ans in self.singleTranspostions():
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
        print("\n The incorrectly spelled word is: " + str(self.word) + "\nIt's line is: ")
        print(self.line)
        print("Here is a list of possible intended words, along with an index showing how close they are to the"
              " original. Lower is closer to the original")
        for i in range(min(20, len(ist))):
            print("Index = " + str(i) + str(ist[i]))
        sentence = ("Enter the index of the word you want to replace the misspelled one. If you don't want to replace "
                    "the word, enter -1. Enter -2 if you want to replace with a custom word")
        i = int(input(sentence))
        if i == -1:
            return (self.word, 0)
        if i == -2:
            return (input("Enter the word you want"), 0)
        if 0 <= i <= min(20, len(ist)):
            upper = int(input("If you want the first letter to be capitalized, enter 1"))
            if upper == 1:
                return (ist[i][0].capitalize(), ist[i][1])
        return ist[i]

    def singleTranspostions(self):
        answer = []
        w = self.word
        for i in range(len(w) - 1):
            new = w[:i] + (w[i + 1] + (w[i] + (w[i + 2:])))
            if new in self.dict:
                answer.append((new, 2))
        return answer

    def permutations(self):
        answer = []
        if len(self.word) < 6:
            for l in permutations(self.word):
                answer.append("".join(l))
        words = []
        for ans in answer:
            if ans in self.dict:
                words.append((ans, 6))
        return words

    def vowelPermutations(self):
        vowels = ""
        indices = []
        for i in range(len(self.word)):
            if self.word[i] in ["a", "e", "i", "u", "o"]:
                vowels = vowels + self.word[i]
                indices.append(i)
        answers = []
        for perm in permutations(vowels):
            new = self.word[:indices[0]] + perm[0]
            for j in range(1, len(vowels)):
                new = new + self.word[indices[j - 1] + 1:indices[j]] + perm[j]
            new = new + self.word[indices[len(vowels) - 1] + 1:]
            if new in self.dict:
                answers.append((new, 4))
        return answers

    def addDouble(self):
        answer = []
        w = self.word
        for i in range(len(w)):
            new = w[:i] + w[i] + w[i:]
            if new in self.dict:
                answer.append((new, 3))
        return answer

    def removeDouble(self):
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
        answer = []
        w = self.word
        print(w)
        print(w)
        letters = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(w) - 1):
            for j in range(26):
                new = w[:i] + letters[j] + w[(i + 1):]
                new = new.strip("\n")
                if new in self.dict:
                    answer.append((new, 5))
        return answer

