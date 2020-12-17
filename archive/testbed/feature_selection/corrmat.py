import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('train.csv')
X = data.iloc[:, 0:20]
y = data.iloc[:, -1]
corrmat = data.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(20,20))
g=sns.heatmap(data[top_corr_features].corr(), annot=True, cmap="RdYlGn")
plt.show()