import numpy as np
import pandas as pd
from scipy.io.arff import loadarff
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

# Convert arff to dataframe
# Ref: https://stackoverflow.com/a/47366936/11806074
raw_data = loadarff('trainset.arff')
df = pd.DataFrame(raw_data[0])

# Decode byte entries to str entries in multiple cols
# Ref: https://stackoverflow.com/a/40390108/11806074
str_df = df.select_dtypes([np.object])
str_df = str_df.stack().str.decode('utf-8').unstack()

# swap out converted cols with the original df cols:
for col in str_df:
    df[col] = str_df[col]

# Number str-type cols
# Ref: https://stackoverflow.com/a/38089089/11806074
# Specificallly, these cols: 'protocol_type', 'service', 'flag'.
df['protocol_type'] = df['protocol_type'].astype('category').cat.codes
df['service'] = df['service'].astype('category').cat.codes
df['flag'] = df['flag'].astype('category').cat.codes

# Convert 'class' into 0 and 1 values.
# Ref: https://stackoverflow.com/a/40902719/11806074
df['class'] = df['class'].map(dict(normal=0, anomaly=1))

# Use only 200 samples
df = df[:200]

# Split dataset into two components: features and labels 
X = df.drop('class', axis=1)
y = df['class']

# Split dataset into trainset and testset with proportion 80/20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Initialize and train classfier
svclassifier = SVC(kernel='linear', max_iter=10000)
svclassifier.fit(X, y)

# Evaluate classification model
y_pred = svclassifier.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# # Export ML model
# from sklearn.externals import joblib
# filename = 'sample_svm_model.sav'
# joblib.dump(svclassifier, filename)

# Others
# to the start/end of line: https://stackoverflow.com/a/38866509/11806074
# Ctrl+Shift+C in vscode opens Terminal in the current working directory.
