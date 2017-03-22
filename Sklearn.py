# coding: utf-8

# #####   Parameters
# data_type 	: 1 for using the original keywords as features, else introducing the positioning effect
# training_part : % of data to use for training the model
# use_saved_cl 	: 1 to use trained model if saved already, else trrain on the data 

from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

from Data import NBC_data, NBC_data_with_pos

import pickle
import random

## Comparision of various classifiers
def Compare_Classifiers(training_set, testing_set):

	## MultinomialNB
	MNB_classifier = SklearnClassifier(MultinomialNB())
	MNB_classifier.train(training_set)
	print("MultinomialNB accuracy percent:",nltk.classify.accuracy(MNB_classifier, testing_set))

	## BernoulliNB
	BNB_classifier = SklearnClassifier(BernoulliNB())
	BNB_classifier.train(training_set)
	print("BernoulliNB accuracy percent:",nltk.classify.accuracy(BNB_classifier, testing_set))

	## LogisticRegression_classifier
	LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
	LogisticRegression_classifier.train(training_set)
	print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

	## SGDClassifier_classifier
	SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
	SGDClassifier_classifier.train(training_set)
	print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

	## SVC_classifier
	SVC_classifier = SklearnClassifier(SVC())
	SVC_classifier.train(training_set)
	print("SVC_classifier accuracy percent:", (nltk.classify.accuracy(SVC_classifier, testing_set))*100)

	## LinearSVC_classifier
	LinearSVC_classifier = SklearnClassifier(LinearSVC())
	LinearSVC_classifier.train(training_set)
	print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

	## NuSVC_classifier
	NuSVC_classifier = SklearnClassifier(NuSVC())
	NuSVC_classifier.train(training_set)
	print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)



if __name__ == "__main__":

	data_type     	= 0 	# 1 for using the original words as features 
	training_part 	= 0.8 	# 80% of data will be used for training 
	use_saved_cl  	= 0 	# Will not used saved, trained model

	if data_type == 1:
		data = NBC_data   ## Without positioning effect
	else:
		data = NBC_data_with_pos

	random.shuffle(data)  ## Shuffle the data for before dividing in training and testing
	cut_off = int(training_part * len(data)) ## Training data observations
	training_set = data[:cut_off]
	testing_set = data[cut_off:]
	random.shuffle(data)

	Compare_Classifiers(training, testing)