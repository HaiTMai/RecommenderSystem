#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 23:08:07 2018

@author: haimai
"""

import sys
import gc

sys.path.insert(0, './Datalib')
sys.path.insert(0, './Model')
from DataLib import DataLoader
from SimpleModels import ContentBased,SimpleCollaborativeFilter
from DeepModels import CollaborativeFilter,DeepCF,ShallowCF

gc.collect()
        
dLoader = DataLoader()
[movies,users,ratings] = dLoader.GetData()

model =ContentBased(movies)
model.Recommend('Dangerous Minds (1995)',20)

# model =SimpleCollaborativeFilter(ratings)
# model.DownSample()
# model.Train()
# model.Evaluate()

# model = ShallowCF(movies,users,ratings)
# model.LoadData()
# model.CreateInputs()
# model.CreateModel()
# print('-------------------- Show Model and Start Training ------------------------------')
# model.ShowModel()
# model.TrainModel()



