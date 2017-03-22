# coding: utf-8

from textblob.classifiers import NaiveBayesClassifier as NBC
from textblob import TextBlob
import pickle
##############################################################################################################

# Function to remove word position identifier, if added earlier
def remove_pos(input_text):
	words = input_text.split() 
	new_text = []
	for i, word in enumerate(words):
		if i < 3: ## For first 3 words in a sentence
			new_text.append(word[:-1])
		else:
			new_text.append(word)

	new_text = " ".join(new_text)
	return new_text 

### Naive Bayes Classifier	
def My_Classifier(training, test, use_saved_cl, cutoff_prob, prediction_only, prob_chk, test__data, data_type):

	model = NBC(training) 

	## Save trained classifier
	if use_saved_cl != 1:
		save_classifier = open("naivebayes.pickle","wb")
		pickle.dump(model, save_classifier)
		save_classifier.close()

	## Use saved trained classifier
	if use_saved_cl == 1:
		classifier_f = open("naivebayes.pickle", "rb")  
		model = pickle.load(classifier_f)
		classifier_f.close()

	if prediction_only != 1:
		print "Model accuracy on test data:", model.accuracy(test)
	else:
		test = test__data

	#### Probabilities
	## Check maximum probability of a class when assigning
	if prob_chk == 1:
		Prob_Check =  open('Class_Assigning_Probabilities_on_Test_Data.txt','w')
		Prob_Check.write('Sentence'+','+ 'Label' + ',' + 'Max_Prob' + ',' + 'Org_Class' + '\n')

		for obs in test:
			if prediction_only == 1:
				sentence = obs
				org_class = 'None'
			else:
				sentence = obs[0]
				org_class = obs[1]

			label = model.classify(sentence)  # assigned label
			probabilities = model.prob_classify(sentence)
			max_prob = 0
			for sample in probabilities.samples():
				if probabilities.prob(sample) > max_prob:
					max_prob = probabilities.prob(sample)

			if (data_type != 1 and prediction_only != 1):
				sentence = remove_pos(str(sentence))
			Prob_Check.write(sentence + ',' + label + ',' + str(max_prob) + ',' + org_class + '\n')	

		Prob_Check.close()

	## Assign class 'unknown' if all probabilities are insignificant
	Results =  open('Results.txt','w')
	Results.write('Sentence'+','+ 'Label' + ',' + 'Max_Prob' + ',' + 'Org_Class' + '\n')

	for obs in test:
		if prediction_only == 1:
			sentence = obs
			org_class = 'None'
		else:
			sentence = obs[0]
			org_class = obs[1]

		label = model.classify(sentence)
		probabilities = model.prob_classify(sentence)
		max_prob = 0
		for sample in probabilities.samples():
			if probabilities.prob(sample) > max_prob:
				max_prob = probabilities.prob(sample)
		if max_prob < cutoff_prob:
			label = 'unknown'
			max_prob = 99

		if (data_type != 1 and prediction_only != 1):
			sentence = remove_pos(str(sentence))
		Results.write(str(sentence) + ',' + label + ',' + str(max_prob) + ',' + org_class + '\n')
		
	Results.close()

