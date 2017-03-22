# coding: utf-8

import re
import pandas as pd

#  Reading the training data file
f = open('LabelledData (1).txt','r')
data = f.read().split('\n')

# Sample code to remove noisy words from a text
noise_list = []
# noise_list = ["is", "a", "in", "the", "this", "on", "into", "for", "of"] 
def remove_noise(input_text):
    words = input_text.split() 
    noise_free_words = [word for word in words if word not in noise_list] 
    noise_free_text = " ".join(noise_free_words) 
    noise_free_text = noise_free_text.decode("utf8").encode('ascii','ignore')
    return noise_free_text

## Update words based on position in the sentence
def word_pos(input_text):
	words = input_text.split() 
	new_text = []
	for i, word in enumerate(words):
		if i < 3: ## For first 3 words in a sentence
			new_text.append(word + str(i))
		else:
			new_text.append(word)

	new_text = " ".join(new_text)
	return new_text 


# Extract sentences and classes into different variables
sentences = []
sentences_with_pos = []
classes = []

for row in data: 
	if len(row) != 0:
		noise_free = remove_noise(row.split(',,,')[0])
		sentences.append(noise_free)
		sentences_with_pos.append(word_pos(noise_free))
		classes.append(row.split(',,,')[1].strip())
		word_pos


NBC_data = zip(sentences,classes)
NBC_data_with_pos = zip(sentences_with_pos,classes)
