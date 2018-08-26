# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
mydataset = pd.read_csv('kidney_disease.csv')
mydataset.info()
mydataset.head()
for i in ['rc','wc','pcv']:
    mydataset[i] = mydataset[i].str.extract('(\d+)').astype(float)
for i in ['age','bp','sg','al','su','bgr','bu','sc','sod','pot','hemo','rc','wc','pcv']:
    mydataset[i].fillna(mydataset[i].mean(),inplace=True)
    mydataset.isnull().sum()
 print("blood test:")
 sns.countplot(data=mydataset,x='rbc')
mydataset['rbc'].fillna('normal',inplace=True)
 print("rbc level is normal")
 sns.countplot(data=mydataset,x='bp')
mydataset['bp'].fillna('normal',inplace=True)
 print("bp level is normal")
 sns.countplot(data=mydataset,x='su')
 mydataset['su'].fillna('normal',inplace=True)
 print("su level is normal")
mydataset['bgr'].fillna('abnormal',inplace=True)
 sns.countplot(data=mydataset,x='bgr')
 print("bgr level is abnormal")
 print("urine test:");
 sns.countplot(data=mydataset,x='al')
mydataset['al'].fillna('abnormal',inplace=True)
 print("albumin level is abnormal")
sns.countplot(data=mydataset,x='pot')
mydataset['pot'].fillna('abnormal',inplace=True)
 print("potassium level is abnormal" )
x=30
if x<=30:
    print("urine level is normal and no kidney failure")
else:
    print("urine level is abnormal and kidney failure identified")
x=60
if x>=60:
    print("GFR level is normal and no kidney failure")
else:
    print("GFR level is mid and chances of kidney failure")

    
        