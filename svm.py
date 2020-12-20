import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.externals import joblib

# Import the dataset
df = pd.read_csv('data/Data.csv')

# Splitting dataset into features and label
X = df.drop('Class', axis=1)
y = df['Class']

# Splitting the dataset into the training set and the test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Feature scaling (or standardization)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Fitting SVM with the training set
classifier = SVC(kernel='rbf', random_state=0)
classifier.fit(X_train, y_train)

# Testing the model by classifying the test set
y_pred = classifier.predict(X_test)

# Creating confusion matrix for evaluation
cm = confusion_matrix(y_test, y_pred)
cr = classification_report(y_test, y_pred)

# Print out confusion matrix and report
print(cm)
print(cr)

# # Export model
# filename = 'ml_model.sav'
# joblib.dump(classifier, filename)
# print("Model exported!")
