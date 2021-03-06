# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 14:09:04 2019

@author: Odysseus
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dill as pickle

from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.model_selection import cross_validate
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.EState.Fingerprinter import FingerprintMol
from rdkit.Chem.rdmolops import RDKFingerprint

Morgan_fingerprint=[]
Estate_fingerprint=[]
RDKit_fingerprint=[]

# Read in the data of gaps
RF_on_gap_data1 = pd.read_excel("E:\\cloud\\Dropbox\\1_paper_proj\\1_bm\\results\\GBRF_KRR\\log_Fbench_values_used_v4_GBRF.xlsx",sheet_name="SMILE_GAP")

# A quick overview of  the data
print(RF_on_gap_data1.describe())

#Convert experimental value column to Numpy arrays
Experimental_Gap = RF_on_gap_data1['Exp'].values

# Print out the SMILE data to verify proper read in SMILE (Special characters in SMILE are properly stored.)
# Also calculate the corresponding Morgan finger print
for Gap_opt_RF_SMILE in RF_on_gap_data1['SMILE']:
    #print (Gap_opt_RF_SMILE)
    # translate mol from its SMILE formula
    mol = Chem.MolFromSmiles(Gap_opt_RF_SMILE)
    
    # calculate the Morgan fingerprint 
    #print(AllChem.GetMorganFingerprintAsBitVect(mol,2,nBits=1024).ToBitString())
    Morgan_fingerprint.append(AllChem.GetMorganFingerprintAsBitVect(mol,2,nBits=1024))
    
    # calculate the Estate fingerprint
    #print(FingerprintMol(mol)[0])
    Estate_fingerprint.append(FingerprintMol(mol)[0])
    
    # calculate the RDKit fingerprint
    RDKit_fingerprint.append(RDKFingerprint(mol, fpSize=1024))
    

# Morgan_fingerprint and bandgaps using RF model
# use sorted(sklearn.metrics.SCORERS.keys()) to find what are available in sklearn lib
RF_on_gap_Morgan = GridSearchCV(RandomForestRegressor(), cv=8, param_grid={"n_estimators": np.linspace(50, 300, 25).astype('int')},scoring='neg_mean_absolute_error', n_jobs=-1)
RF_on_gap_Morgan.fit(Morgan_fingerprint, Experimental_Gap)

Best_RF_on_gap_Morgan = RF_on_gap_Morgan.best_estimator_
print("Best parameters", RF_on_gap_Morgan.best_params_)
print("Score function used", RF_on_gap_Morgan.scorer_)
print("Score for the best tuning", -1*RF_on_gap_Morgan.best_score_)
print("fitting time", RF_on_gap_Morgan.refit_time_)

save_model_parameter_RF_on_gap_Morgan = 'RF_on_gap_Morgan.sav'
pickle.dump(RF_on_gap_Morgan, open(save_model_parameter_RF_on_gap_Morgan, 'wb'))




# Estate_fingerprint and bandgaps using RF model
# use sorted(sklearn.metrics.SCORERS.keys()) to find what are available in sklearn lib
RF_on_gap_Estate = GridSearchCV(RandomForestRegressor(), cv=8, param_grid={"n_estimators": np.linspace(50, 300, 25).astype('int')}, scoring='neg_mean_absolute_error', n_jobs=-1)
RF_on_gap_Estate.fit(Estate_fingerprint, Experimental_Gap)

Best_RF_on_gap_Estate = RF_on_gap_Estate.best_estimator_
print("Best parameters",RF_on_gap_Estate.best_params_)
print("Score function used",RF_on_gap_Estate.scorer_)
print("Score for the best tuning",-1*RF_on_gap_Estate.best_score_)
print("fitting time",RF_on_gap_Estate.refit_time_)

save_model_parameter_RF_on_gap_Estate = 'RF_on_gap_Estate.sav'
pickle.dump(RF_on_gap_Estate, open(save_model_parameter_RF_on_gap_Estate, 'wb'))


# RDKit_fingerprint and bandgaps using RF model
# use sorted(sklearn.metrics.SCORERS.keys()) to find what are available in sklearn lib
RF_on_gap_RDKit = GridSearchCV(RandomForestRegressor(), cv=8, param_grid={"n_estimators": np.linspace(50, 300, 25).astype('int')}, scoring='neg_mean_absolute_error', n_jobs=-1)
RF_on_gap_RDKit.fit(RDKit_fingerprint, Experimental_Gap)

Best_RF_on_gap_RDKit = RF_on_gap_RDKit.best_estimator_
print("Best parameters",RF_on_gap_RDKit.best_params_)
print("Score function used",RF_on_gap_RDKit.scorer_)
print("Score for the best tuning",-1*RF_on_gap_RDKit.best_score_)
print("fitting time",RF_on_gap_RDKit.refit_time_)


save_model_parameter_RF_on_gap_RDKit = 'RF_on_gap_RDKit.sav'
pickle.dump(RF_on_gap_RDKit, open(save_model_parameter_RF_on_gap_RDKit, 'wb'))






