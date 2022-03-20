# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:58:33 2019

@author: Yifu 

Keras Autoencoder test1 

updated 2019/03/12 - second time
updated 2021/06/26 - local repository 

"""

import os
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from numpy.random import seed
from sklearn.preprocessing import minmax_scale
from sklearn.model_selection import train_test_split
from keras.layers import Input, Dense
from keras.models import Model

#print(os.listdir("./"))

train = pd.read_csv('ae_train.csv')
test = pd.read_csv('ae_test.csv')

target = train['target']
train_id = train['ID']
test_id = test['ID']

train.drop(['target'], axis=1, inplace=True)
train.drop(['ID'], axis=1, inplace=True)
test.drop(['ID'], axis=1, inplace=True)

print('Train data shape', train.shape)
print('Test data shape', test.shape)

train_scaled = minmax_scale(train, axis = 0)
test_scaled = minmax_scale(test, axis = 0)

train_scaled = minmax_scale(train)
test_scaled = minmax_scale(test)


train_scaled = pd.DataFrame(train_scaled, columns = list(train))


#--------- design autoencoder --------------- 
# define the number of features
ncol = train_scaled.shape[1]

X_train, X_test, Y_train, Y_test = train_test_split(train_scaled, target, train_size = 0.9, random_state = 0)

### Define the encoder dimension
encoding_dim = 200

input_dim = Input(shape = (ncol, ))

# Encoder Layers
encoded1 = Dense(50, activation = 'relu')(input_dim)
encoded2 = Dense(20, activation = 'relu')(encoded1)
encoded3 = Dense(encoding_dim, activation = 'relu')(encoded2)

# Decoder Layers
decoded1 = Dense(20, activation = 'relu')(encoded3)
decoded2 = Dense(50, activation = 'relu')(decoded1)
decoded3 = Dense(ncol, activation = 'sigmoid')(decoded2)

# Combine Encoder and Deocder layers
autoencoder = Model(inputs = input_dim, outputs = decoded3)

# Compile the Model
autoencoder.compile(optimizer = 'adadelta', loss = 'binary_crossentropy')
autoencoder.summary()

autoencoder.fit(X_train, X_train, nb_epoch = 10, batch_size = 32, shuffle = False)  # , validation_data = (X_test, X_test))

encoder = Model(inputs = input_dim, outputs = encoded3)
encoded_input = Input(shape = (encoding_dim, ))

encoded_train = pd.DataFrame(encoder.predict(train_scaled))
encoded_train = encoded_train.add_prefix('feature_')

encoded_test = pd.DataFrame(encoder.predict(test_scaled))
encoded_test = encoded_test.add_prefix('feature_')

encoded_train['target'] = target

print(encoded_train.shape)
encoded_train.head()

print(encoded_test.shape)
encoded_test.head()

encoded_train.to_csv('ae_train_encoded.csv', index=False)
encoded_test.to_csv('ae_test_encoded.csv', index=False)













