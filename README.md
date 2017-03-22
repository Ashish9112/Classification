
## Task 
Identify Question Type: Given a question, the aim is to identify the category it belongs to. The four categories to handle: Who, What, When, Affirmation(yes/no). <br />
Label any sentence that does not fall in any of the above four as "Unknown" type.

## Example
1. What is your name? Type: What

2. When is the show happening? Type: When

3. Is there a cab available for airport? Type: Affirmation

## Sample Data
what 's the second-most-used vowel in english ? ,,, what <br />
who was the inventor of silly putty ? ,,, who <br />
what is the highest waterfall in the united states ? ,,, what <br />
name a golf course in myrtle beach . ,,, unknown <br />
which two states enclose chesapeake bay ? ,,, unknown <br />
what does the abbreviation aids stand for ? ,,, what <br />
what does a spermologer collect ? ,,, what <br />

## Algorithms Used:
Naive Bayes Classifier (Reference: http://textblob.readthedocs.io/en/dev/classifiers.html)

## Codes:
Data.py - Read the input data file. Do cleaning, transformation etc. <br />
Classifier.py - Train the model on the data and predict class for test observations <br />
Models.py - Takes input arguments from user, calls function 'Data.py' and 'Classifier.py'. Save the results in the files. <br />
Sklearn.py - Compare various classifiers based on the accuracy and select the best one among them.[Need some modification for input data type] <br />

## How to use
Just execute the code "Models.py" <br />

### Parameters to play with models
data_type      > [default = 0 > To take into effect word's position(Explaination in sec 1.1 below), any other value otherwise] <br />
training_part   [default = 0.8 > How much part of data will be used for training] <br />
use_saved_cl    [default = 0 	> Will train model on training data, otherwise use saved trained model] <br />
cutoff_prob     [default = 0.9 > If all predicted class probabilities falls below this number, it will assign class "unknown"] <br />
prediction_only [default = 0 > Nonzero values if only want to predict class (on new dataset for which we don't know actual class)] <br />
prob_chk        [default = 0 > Nonzero value will save predicted class with the probability on which they have been assigned] <br />

