"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Finds words"""
    def __init__(self, file):
        self.word_list = []
        self.get_words(file)


        
    def get_words(self, file):
        word_file = open(file, "r")

        for line in word_file:
            self.word_list.append(line.replace("\n", ""))

        word_file.close()

        print(f"There are {len(self.word_list)} words")

    def random(self):
        return random.choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """improves WordFinder"""
    def __init__(self, file):
        super().__init__(file)

    def get_words(self, file):
        word_file = open(file, "r")

        for line in word_file:
            if line[0] != "#" and line != "\n":
                self.word_list.append(line.replace("\n", ""))

        word_file.close()

        print(f"There are {len(self.word_list)} words")

