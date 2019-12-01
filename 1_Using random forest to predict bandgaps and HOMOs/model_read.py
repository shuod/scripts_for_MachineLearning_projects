# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 00:11:42 2019

@author: Odysseus
"""

import dill as pickle
from sklearn.model_selection import GridSearchCV
import numpy as np

mol = Chem.MolFromSmiles('c1ccccc1CC1CC1')

print ('mol')

Morgan_fingerprint = AllChem.GetMorganFingerprintAsBitVect(mol,2,nBits=1024)


model = pickle.load(open("RF_on_gap_Morgan.sav","rb"))

print(model.predict(Morgan_fingerprint.reshape(-1,1)))