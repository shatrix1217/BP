#import modules
import tensorflow as tf

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

import numpy as np
import matplotlib.pyplot as plt

#read file
file_path = "C:\\Users\\Watabe\\Desktop\\kaggle_datasets\\Irish_poem.txt"
with open(file_path, 'r', encoding = 'utf8') as f:
    data = f.read()

#To-Do : initiate tokenizer object and prepare training data
tokenizer = Tokenizer(oov_token = "<OOV>")
corpus = data.lower().split("\n")

tokenizer.fit_on_texts(corpus)

#To-Do : list of tokenized sequences in fibonacci
input_sequences = []
for line in corpus:
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_sequences = token_list[ : i+1 ]
        input_sequences.append(n_gram_sequences)

#To-Do : sequences padding
max_sequences_len = max(len(x) for x in input_sequences)
input_sequences = np.array(pad_sequences(input_sequences, maxlen = max_sequences_len, padding = 'pre'))

#To-Do : separate predictors and labels
total_words = len(tokenizer.word_index) + 1
x_seq, labels = input_sequences[ : , : -1], input_sequences[ : , -1]
y_seq = tf.keras.utils.to_categorical(labels, num_classes = total_words)

#To-Do : keras sequential model building
model = Sequential()
model.add(Embedding(total_words, 100, input_length=max_sequences_len-1))#deduct y
model.add(Bidirectional(LSTM(150)))
model.add(Dense(total_words, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=0.01), metrics=['accuracy'])
history = model.fit(x_seq, y_seq, epochs=20, verbose=1)
print(model)

#To-Do : visualizing accuracy
def plot_graphs(history, string):
    plt.plot(history.history[string])
    plt.xlabel('Epochs')
    plt.ylabel(string)
    plt.show()

plot_graphs(history, 'accuracy')

#To-Do : make the model write a poem
start_text = "Roses are red, violets are blue"
next_words = 100

for i in range(next_words):
    token_list = tokenizer.texts_to_sequences([start_text])[0]
    token_list = pad_sequences([token_list], maxlen =   max_sequences_len-1, padding='pre')
    predicted = model.predict_classes(token_list, verbose = 0)
    output_word = ' '
    for word, index in tokenizer.word_index.items():
        if index == predicted:
            output_word = word
            break
    start_text += " " + output_word
print(start_text)