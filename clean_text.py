# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 12:20:02 2018

@author: shl12
"""

from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer

# Init Objects
tokenizer = RegexpTokenizer(r'\w+')
en_stopwords = set(stopwords.words('english'))
#print(len(en_stopwords))
en_stopwords.difference_update({'very','again','not',"doesn't","don't","isn't"})
#print(len(en_stopwords))
ps = PorterStemmer()


def getCleanReview(review):
    review = str(review) # if review is numpy array
    review = review.lower()
    review = review.replace("<br /><br />"," ")
    
    #Tokenize
    tokens = tokenizer.tokenize(review)
    new_tokens = [token for token in tokens if token not in en_stopwords]
    stemmed_tokens = [ps.stem(token) for token in new_tokens]
    
    cleaned_review = ' '.join(stemmed_tokens)
    
    return cleaned_review
    
