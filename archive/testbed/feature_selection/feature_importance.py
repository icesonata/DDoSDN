import pandas as pd
import numpy as np

data = pd.read_csv('train.csv')
X = data.iloc[:, 0:20]
y = data.iloc[:, -1]

from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt

model = ExtraTreesClassifier()
model.fit(X, y)
# print(model.feature_importances_)

feat_importances = pd.Series(model.feature_importances_, index=X.columns)
feat_importances.nlargest(10).plot(kind='barh')
plt.show()

