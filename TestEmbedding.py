#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 00:25:09 2018

@author: haimai
"""

from __future__ import division, print_function
import numpy as np
import pandas as pd
import gc

from keras.layers import Input, Embedding, merge, Flatten, Dense, Dropout,dot,add,concatenate
from keras.regularizers import l2
from keras.models import Model,Sequential
from keras.optimizers import Adam
from keras import backend as K


model = Sequential()
model.add(Embedding(1000, 64, input_length=3))
# the model will take as input an integer matrix of size (batch, input_length).
# the largest integer (i.e. word index) in the input should be no larger than 999 (vocabulary size).
# now model.output_shape == (None, 10, 64), where None is the batch dimension.

input_array = np.random.randint(1000, size=(5,3))

model.compile('rmsprop', 'mse')
output_array = model.predict(input_array)
print(output_array.shape)
assert output_array.shape == (32, 1, 64)