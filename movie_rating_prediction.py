# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 16:01:39 2018

@author: shl12
"""

# Importing the libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import clean_text as ct
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB,BernoulliNB,GaussianNB

# Importing the dataset

X_train = pd.read_csv('dataset/imdb_trainX.txt',sep = '\n',header = None).values
Y_train = pd.read_csv('dataset/imdb_trainY.txt',sep = '\n',header = None).values.reshape((-1,))
X_test = pd.read_csv('dataset/imdb_testX.txt',sep = '\n',header = None).values
Y_test = pd.read_csv('dataset/imdb_testY.txt',sep = '\n',header = None).values.reshape((-1,))

print(type(X_train))
print(X_train.shape)
print(Y_train.shape)
print(X_test.shape)
print(Y_test.shape)