# coding: utf-8

# #####   Parameters
# data_type 	: 1 for using the original keywords as features, else introducing the positioning effect
# training_part : % of data to use for training the model
# use_saved_cl 	: 1 to use trained model if saved already, else trrain on the data 
# cutoff_prob 	: Below this probability, lables will be assigned as "unknown" 
# prob_chk		: 1 to write test class assigining probabilities info into file "Class_Assigning_Probabilities_on_Test_Data"

from Data import NBC_data, NBC_data_with_pos
from Classifier import My_Classifier
import pickle
import random

## Train and test on model on the data
def Run_Model(data , training_part, use_saved_cl, cutoff_prob, prediction_only, prob_chk, test__data, data_type):

	random.shuffle(data)  ## Shuffle the data for before dividing in training and testing

	cut_off = int(training_part * len(data)) ## Training data observations
	training = data[:cut_off]
	test = data[cut_off:]

	My_Classifier(training, test, use_saved_cl, cutoff_prob, prediction_only, prob_chk, test__data, data_type)


if __name__ == "__main__":

	data_type     	= 0 	# 1 for using the original words as features 
	training_part 	= 0.8 	# 80% of data will be used for training 
	use_saved_cl  	= 0 	# Will not used saved, trained model
	cutoff_prob   	= 0.9 
	prediction_only = 0
	prob_chk = 0

	if data_type == 1:
		data = NBC_data   ## Without positioning effect
	else:
		data = NBC_data_with_pos

	test__data = ['What is the name of US prez ?','why do we feel pain?']

	if prediction_only == 1:
		training_part = 1	# train on whole dataset
	else: 
		test__data = []

	Run_Model(data, training_part, use_saved_cl, cutoff_prob, prediction_only, prob_chk, test__data, data_type)

