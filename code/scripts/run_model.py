from collections import Counter
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
import pickle
import pandas as pd
import numpy as np
import sys
import os


def read_parse_input(filepath):
    data = [i.strip('\n').split('\t') for i in open(filepath, 'r', encoding='utf8', errors='ignore')]
    X = []
    Y = []
    for i in range(len(data)):
        if i % 2 == 0:
            X.append(' '.join(data[i]))
        else:
            Y.append(data[i])

    # remove labels with less than two occurrences
    all_labels = [label for list in Y for label in list]
    counter = Counter(all_labels)

    n_most_common = counter.most_common()
    
    for i in range(len(n_most_common)):
        if n_most_common[i][1] < 2:
            for j in range(len(Y)):
                if n_most_common[i][0] in Y[j]:
                    Y[j].remove(n_most_common[i][0])

    return X, Y


def train_one_v_rest_and_pred(X_train, Y_train, X_test, Y_test):
    predictions = np.zeros(Y_test.shape)
    classifiers = []
    for i in range(len(Y_train[0])):
        this_train = [l[i] for l in Y_train]
        if 1 not in this_train: # <- only needed if class not represented in training set
            break
        else: 
            lr = LogisticRegression(class_weight={0:1, 1:150})
            lr.fit(X_train, this_train)
            classifiers.append(lr)
            preds = lr.predict(X_test)

        #set predictions in predictions matrix
        for j in range(len(preds)):
            if preds[j] == 1:
                predictions[j][i] = 1

    return predictions

vectorizer = pickle.load(open("../pickle_files/vectorizer.pickle", "rb"))
mlb = pickle.load(open("../pickle_files/multi-label_binarizer.pickle", "rb"))
X, Y = read_parse_input(sys.argv[0])
X_trans = vectorizer.transform(X)
Y_trans = mlb.transform(Y)
X_test, Y_test = read_parse_input(sys.argv[1])
X_test_trans = vectorizer.transform(X_test)
Y_test_trans = mlb.transform(Y_test)
preds = train_one_v_rest_and_pred(X_trans, Y_trans, X_test_trans, Y_test_trans)
f1_score = f1_score(Y_test_trans, preds, average='macro')
print("F1 score:", f1_score)