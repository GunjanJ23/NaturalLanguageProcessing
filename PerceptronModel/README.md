## Overview:
In this assignment, the following perceptron classifiers (vanilla and averaged) were implemented to identify hotel reviews as either
true or fake, and either positive or negative. 

The word tokens as features, or any other features can be devised from the text.

## Data:
The training and development data were available as a compressed ZIP archive. The uncompressed archive contains the following files:

• One file train-labeled.txt containing labeled training data with a single training instance (hotel review) per line (total 960 lines).

The first 3 tokens in each line are:

1.a unique 7-character alphanumeric identifier

2.a label True or Fake

3.a label Pos or Neg

These are followed by the text of the review.

• One file dev-text.txt with unlabeled development data, containing just the unique identifier followed by the text of the review
(total 320 lines).

• One file dev-key.txt with the corresponding labels for the development data, to serve as an answer key.

## Programs:

Two programs: perceplearn.py will learn perceptron models (vanilla and averaged) from the training data, and percepclassify.py will
use the models to classify new data.
