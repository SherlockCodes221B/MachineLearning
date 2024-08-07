# -*- coding: utf-8 -*-
"""Income_predict.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Dt6IhjErNaZ2ttBoDRoZJPp-mifhGwND
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('/content/adult.csv')
data.head()

data.info()

data.isnull().sum()

data.drop(columns=['fnlwgt'],inplace=True)

data = pd.concat([data.drop('occupation',axis=1),pd.get_dummies(data.occupation,dtype=int).add_prefix('occupation_')],axis=1)
data = pd.concat([data.drop('workclass',axis=1),pd.get_dummies(data.workclass,dtype=int).add_prefix('workclass_')],axis=1)
data = pd.concat([data.drop('relationship',axis=1),pd.get_dummies(data.relationship,dtype=int).add_prefix('relationship_')],axis=1)
data = pd.concat([data.drop('race',axis=1),pd.get_dummies(data.race,dtype=int).add_prefix('race_')],axis=1)
data = pd.concat([data.drop('native-country',axis=1),pd.get_dummies(data['native-country'],dtype=int).add_prefix('native-country_')],axis=1)
data = pd.concat([data.drop('marital-status',axis=1),pd.get_dummies(data['marital-status'],dtype=int).add_prefix('marital-status_')],axis=1)

data

data.drop(columns= ['education'],inplace=True)

data['gender'] = data['gender'].map({'Male':0,'Female':1})
data['income'] = data['income'].map({'<=50K':0,'>50K':1})
data.head()

plt.figure(figsize=(15,10))
sns.heatmap(data.corr(),annot=False,cmap='coolwarm')

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data.info()

train_df,test_df =  train_test_split(data,test_size=0.2,random_state=42)

train_X = train_df.drop(columns=['income'])
train_y = train_df['income']
test_X = test_df.drop(columns=['income'])
test_y = test_df['income']

forest = RandomForestClassifier()
forest.fit(train_X,train_y)

forest.score(test_X,test_y)

forest.feature_importances_

model = LogisticRegression()
model.fit(train_X,train_y)

model.score(test_X,test_y)