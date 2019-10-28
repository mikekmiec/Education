
# HW 4 CSE 163 Part 1

import math
import os
import re
from document import Document

class SearchEngine:
    '''
    This class contains information about the documents on the directory and
    searches the related documents.
    '''
    def __init__(self, dir):
        """
        Constructs a new SearchEngine object with the given directory name.
        It contains set of the documents, set of all words, inverse
        index, and the dictionary of word: IDF of the word.
        """
        self._dname = dir
        self._docs = set()
        for file in os.listdir(dir):
            doc = Document(dir + '/' + file)
            self._docs.add(doc)
        self._all_words = self._get_all_words()
        self._inverse_index = self._get_inverse_index()
        self._word_idf = dict()
        for word in self._all_words:
            self._word_idf[word] = self._calculate_idf(word)
        
        
        
    def _get_all_words(self):
        '''
        This function creates a list of all words in all documents.
        '''
        word_set = set()
        for doc in self._docs:
            for word in doc.get_words:
                word_set.add(word)
        return word_set
    
    def _get_inverse_index(self):
        '''
        This function returns the documents that contains the term.
        '''
        d = dict()
        for word in self._all_words:
            doc_list = list()
            for doc in self._docs:
                if word in doc.get_words:
                    doc_list.append(doc)
            d[word] = doc_list
        return d
    
    
    def _calculate_idf(self, term):
        '''
        This function takes a term as a string argument and returns the score
        for that term over all documents managed by search engine.
        '''
        if term not in self._all_words:
            return 0
        count_term = len(self._inverse_index(term))
        doc_count = len(self._docs)
        return math.log(doc_count/count_term)
    
    
    def _get_word_idf(self, term):
        '''
        This function returns the idf for the term.
        '''
        if term not in self._all_words:
            return 0
        else:
            return self._word_idf[term]
        
        
    
    def _search(self, string):
        '''
        This function takes a term and returns a list of docuemnts.
        '''
        doc_tfidf = list()
        words = string.split()
        wlist = list()
        for word in words:
            word = word.lower()
            word = re.sub(r'\W+', '', word)
            wlist.append(word)
        count = 0
        for word in wlist:
            if word in self._all_words:
                count += 1
        if count == 0:
            return None
        else:
            for doc in self._docs:
                score = 0
                for word in wlist:
                    if word in doc.get_words():
                        score += doc.term_frequency(word)*self._word_idf[word]
                    if score != 0:
                        doc_tfidf.append(doc.get_name(), score)
            sorted_list = sorted(doc_tfidf, key=lambda f: f[1], reverse=True)
            return [t[0] for t in sorted_list]
            
        
        
    def get_dname(self):
        """
        Returns the directory name
        """
        return self._dname
        

        
