from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        self.path = path
        self.words = self.get_words()

    def get_words(self):
        word_file = open(self.path, "r")
        words = []
        for line in word_file:
            words.append(line)
        word_file.close()
        return words

    def get_random(self):
        return choice(self.words)


word_instance = WordFinder("words")
print(word_instance.words)
print(word_instance.get_random())