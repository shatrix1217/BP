#import modules
import tensorflow as tf

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

import numpy as np 

#read file
data = open(C:\\Users\\Watabe\\Desktop\\kaggle_datasets\\Irish_poem.txt).read

#To-Do : initiate tokenizer object and prepare training data
tokenizer = Tokenizer(oov_token = "<OOV>")
corpus = data.lower().split("\n")

tokenizer.fit_on_texts(corpus)
print(tokenizer.word_index)

#To-Do : list of tokenized sequences in fibonacci, quite confusing

#To-Do : sequences padding

#To-Do : separate predictors and labels

#To-Do : keras sequential model building

#To-Do : visualizing accuracy

#To-Do : make the model write a poem
"Roses are red, violets are blue"