## Using random forest to predict bandgaps and HOMOs

Goal: Random forest method was tested in order to be compared against traditional DFT/TD-DFT methods.

Method: check my blog article:

**Results(cv=8):**

1. Mean absolute error (MAE) when using random forest to predict bandgap:
- Morgan fingerprint: MAE=0.4219 (number\_of\_trees=122)
- Estate fingerprint: MAE=0.3959 (number\_of\_trees=60)
- RDKit fingerprint: MAE=0.4268 (number\_of\_trees=164)

**Compared to**
Results from the chosen functional after benchmarking study in phase1 (HSE06) in academic project 1 gives:

- Before additional linear correction MAE=0.21
- After additional linear correction MAE=0.15

2. Mean absolute error (MAE) when using random forest to predict bandgap:
- Morgan fingerprint: MAE=0.1519 (number\_of\_trees=60)
- Estate fingerprint: MAE=0.1640 (number\_of\_trees)=91)
- RDKit fingerprint: MAE=0.1467 (number\_of\_trees=216)

**Compared to**
Results from the chosen functional after benchmarking study in phase1 (HSE06) in academic project 1 gives:

- Before additional linear correction MAE=0.18
- After additional linear correction MAE=0.13

**Optimization of two other most important hyper-parameters of random forest model(number of feature used when splitting or max_features, maximum levels in each decision tree or max_depth) will be performed in the future.**

**Script:**

- <u>*p2\_RF\_on\_gap.py*</u>: Python script to use random forest to predict bandgap.

- <u>*p2\_RF\_on\_HOMO.py*</u>: Python script to use random forest to predict HOMO.