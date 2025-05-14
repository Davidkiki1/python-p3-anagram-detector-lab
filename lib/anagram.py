class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        '''Returns a list of words that are anagrams of the initialized word.'''
        return [anagram for anagram in possible_anagrams if sorted(anagram) == sorted(self.word)]