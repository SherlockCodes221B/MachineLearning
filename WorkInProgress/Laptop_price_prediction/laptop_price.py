# -*- coding: utf-8 -*-
"""Laptop_price.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZQmROz80b-p8OxEABhupKdBdhWVOosSh

Import Libraries
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/LaptopPrice/laptop_data.csv')
data.info()

data.drop(columns=['Unnamed: 0'], inplace=True)

data.head()

data['Ram'] = data['Ram'].str.replace('GB','').astype(int)
data['Weight'] = data['Weight'].str.replace('kg','').astype(float)

data['CPU_name'] = data['Cpu'].apply(lambda text:" ".join(text.split()[:3]))

data['Touchscreen'] = data['ScreenResolution'].apply(lambda text:1 if 'Touchscreen' in text else 0)
data['Ips'] = data['ScreenResolution'].apply(lambda text:1 if 'IPS' in text else 0)

data['Resolution'] = data['ScreenResolution'].apply(lambda text:text.split()[-1])
data['Resolution_x'] = data['Resolution'].apply(lambda text:text.split('x')[0])
data['Resolution_y'] = data['Resolution'].apply(lambda text:text.split('x')[1])
data['Resolution_x'] = data['Resolution_x'].astype(int)
data['Resolution_y'] = data['Resolution_y'].astype(int)
data.info()

data['PPI'] = (((data['Resolution_x']**2+data['Resolution_y']**2))**0.5/data['Inches']).astype('float')
data.head()

def apply_logic(text):
  if text in 'Intel Core i5' or text in 'Intel Core i7' or text in 'Intel Core i3':
    return text
  else:
    if text.split()[0] == 'Intel':
      return 'Other Intel Processor'
    else:
      return 'AMD Processor'

data['CPU_name'] = data['CPU_name'].apply(apply_logic)

data['Memory'].value_counts()

data['Memory'] = data['Memory'].astype(str).replace('\.0', '', regex=True)
data["Memory"] = data["Memory"].str.replace('GB', '')
data["Memory"] = data["Memory"].str.replace('TB', '000')
newdf = data['Memory'].str.split("+",n = 1,expand = True)

data['first'] = newdf[0]
data['second'] = newdf[1]
data['column1'] = data['first'].apply(lambda text:text.split()[1])
data['column2'] = data['first'].apply(lambda text:text.split()[0])
data.head()