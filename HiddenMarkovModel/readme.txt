Overview:
In this assignment, a Hidden Markov Model part-of-speech tagger for English, Chinese, and Hindi was implemented. The training data are provided tokenized and tagged; the test data will be provided tokenized, and the tagger will add the tags. 

Data:
A set of training and development data were made available as a compressed ZIP archive.
The uncompressed archive will have the following files:

•Two files (one English, one Chinese) with tagged training data in the word/TAG format, with words separated by spaces and each sentence on a new line.
•Two files (one English, one Chinese) with untagged development data, with words separated by spaces and each sentence on a new line.
•Two files (one English, one Chinese) with tagged development data in the word/TAG format, with words separated by spaces and each sentence on a new line, to serve as an answer key.

Programs:
Two programs: hmmlearn.py will learn a hidden Markov model from the training data, and hmmdecode.py will use the model to tag new data. 
The argument is a single file containing the test data; the program will read the parameters of a hidden Markov model from the file hmmmodel.txt, tag each word in the test data, and write the results to a text file called hmmoutput.txt in the same format as the training data.

