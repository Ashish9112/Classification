Just run thes lines to check if you have all modules installed

### Data.py
import re <br />
import pandas as pd <br />

### Classifier.py
from textblob.classifiers import NaiveBayesClassifier as NBC <br />
from textblob import TextBlob <br />
import pickle <br />

### Models.py
import pickle <br />
import random <br />

### Sklearn.py
from nltk.classify.scikitlearn import SklearnClassifier <br />
from sklearn.naive_bayes import MultinomialNB,BernoulliNB <br />
from sklearn.linear_model import LogisticRegression,SGDClassifier <br />
from sklearn.svm import SVC, LinearSVC, NuSVC <br />
import pickle <br />
import random <br />
