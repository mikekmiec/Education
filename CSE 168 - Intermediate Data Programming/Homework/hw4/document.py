#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 13:27:54 2019
@author: mike
"""
# HW 4 CSE 163 Part 0

import re



class Document:
    def __init__(self, filename):
        '''
        Initializes a new Document object, storing a dictionary of word keys
        and count values as well as the list of unique words.
        '''
        self._filename = filename
        self._word_count_dict = self._compute_word_count_dict(filename)
        self._words = list(self._word_count_dict.keys())
        
    def _compute_word_count_dict(self, filename):
        '''
        This function creates a dictionary with word:count.
        ***case insensitive, remove punctuation.
        '''
        d = dict()
        with open(filename) as n:
            tokens = n.read().split()
            for token in tokens:
                token = token.lower()
                token = re.sub(r'\W+', '', token)
                if token not in d:
                    d[token] = 1
                else:
                    d[token] += 1
        return d

            
    def term_frequency(self, term):
        '''
        This function takes a term as a parameter and returns the frequency of the
        given term in the document. It uses a pre-computed dictionary.
        If word does not exist then function returns 0.
        ***case insensitive, remove punctuation.
        '''
        if term not in self.get_words():
                return 0
        total = sum(self._word_count_dict.values())
        count = self._word_count_dict[term]
        return count/total
    
    
    
    def get_words(self):
        '''
        This function returns a list of all the words in a document.
        '''
        return self._words
    
    def get_filename(self):
        '''
        This function returns the document name.
        '''
        return self._filename
        
    
    

