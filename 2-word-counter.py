"""
Exemplary implementation of word counter.
"""

import json, string
from collections import Counter
from typing import Dict

class WordCounter():
    '''
    Class which counts the number of male and female words in a given text, where the 
    male and female words are given as input files.
    '''

    def __init__(self, text : str, gendered_words : Dict[str, Dict[str, float]]):
        self._text = text
        self._gendered_words = gendered_words
        self._counter = {gender : 0 for gender in self._gendered_words.keys() }
        self._n_words = 0
        self.counts_computed = False
        self.n_words_computed = False


    def get_counts(self):
        self.counts_computed = True
        self.n_words_computed = True

        for word in self._text.split():
            word = process_word(word)
            for gender in self._gendered_words:
                if gender in set(['male_gaucher', 'female_gaucher']):
                    self.increase_counter_gaucher(word, gender)
                else:
                    if word in self._gendered_words[gender]:
                        self._counter[gender] += self._gendered_words[gender][word]
            self._n_words += 1
        
        assert self._n_words > 0, 'the text must not be empty'
        return self.counter


    def get_frequencies(self):
        '''
        Returns the frequencies of male words and female words in the file (note that they do not have to sum to 1).
        '''
        return {key: self.counter[key]/self.n_words for key in self.counter}

    
    def increase_counter_gaucher(self, processed_word : str, gender : str):
        '''
        Check if a word is in the dictionary. Assumes the word is processed. Note it does not check whether it's processed!
        '''

        for key in self._gendered_words[gender].keys():
            if key.endswith('-'):
                if processed_word.startswith(key[:-1]):
                    self._counter[gender] += self._gendered_words[gender][key]
            elif processed_word == key:
                    self._counter[gender] += self._gendered_words[gender][key]
        return False


    @property
    def gendered_words(self):
        return self._gendered_words


    @property
    def counter(self):
        if not self.counts_computed:
            self.get_counts()
        return self._counter


    @property
    def n_words(self):
        if not self.n_words_computed:
            self.get_counts()
        return self._n_words
        

    @property
    def text(self):
        return self._text


def process_word(word : str):
    '''
    Make word lower case and remove punctuation
    '''
    # remove everything after "'" (e.g. Eduard's turns into Eduard)
    if "'" in word:
        word = word.split("'")[0]
    bad_characters = set([chr(char) for char in list(range(45))+list(range(46,65))+list(range(91,97))+list(range(123,161))])
    return ''.join([c for c in word if c not in bad_characters]).lower()

