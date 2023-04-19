from random import choice

class WordFinder:
    """Word Finder: finds random word from a dictionary."""

    def __init__(self, path):
        """creates list of words from file path"""
        word_file = open(path, "r")
        self.words = self.get_words(word_file)
        print(f"words read {len(self.words)}")
        word_file.close()

    def get_words(self, file):
        """returns a list of words from the file path"""
    
        return [line.strip() for line in file]

    def get_random(self):
        """returns a random word from the words list"""
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds a random word from a document ignoring 
    comments and blank lines"""

    def get_words(self, file):
        """returns a list of words with comments and blank lines omitted"""
        word_list = super().get_words(file)
        return [ word for word in word_list 
            if not (word.startswith("#") or word == "")]