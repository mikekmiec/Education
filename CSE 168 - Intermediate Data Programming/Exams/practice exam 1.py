#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:19:39 2019

@author: mike
"""

#Problem 1) Python Programming

def print_every_other_word(file):
    with open(file) as f:
            tokens = f.read().split()
            for token in tokens:
                if token in even position:
                    add to output
            return output
        
#Problem 2) Tabular Data
#2.a.i) max_atk_difference_manual

def max_atk_differemce_manual(df):
    max_atk = 0
    min_atk = 0
    for row in data:
        if row[atk] > max_atk:
            row[atk] == max_atk
        if row[atk] < min_atk:
            row[atk] == min_atk
    return (max_atk - min_atk)
        
#2.a.ii) max_atk_difference_pandas
#2.b) best_matchup_manual
    
def max_atk_differemce_pandas(df):
    return (df.max('atk')-df.min('atk'))
            
#Problem 3) Machine Learning 
#3.a) Train a classifier
#3.b) Featuring
#3.c) Making Predictions
            
#Problem 4) Classes
#4.a) Implementing  Rectangle
#4.b) Using  Rectangle
            
#Problem 5) Big-O Efficiency
#5.a) 
#5.b)
#5.c)
#5.d)