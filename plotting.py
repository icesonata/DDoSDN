# import numpy as np
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.svm import SVC
# from sklearn.metrics import confusion_matrix, classification_report
# import joblib

# # Import the dataset
# df = pd.read_csv('data/dataset.csv')

# # Splitting dataset into features and label
# X = df.drop('Class', axis=1)
# y = df['Class']

# # Splitting the dataset into the training set and the test set
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# # # Feature scaling (or standardization)
# # scaler = StandardScaler()
# # X_train = scaler.fit_transform(X_train)
# # X_test = scaler.transform(X_test)

# # Visualising the Training set results
# # import matplotlib.pyplot as plt
# # from matplotlib.colors import ListedColormap
# # # X_set, y_set = X_train, y_train
# # # X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
# # #                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
# # # plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
# # #             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
# # # plt.xlim(X1.min(), X1.max())
# # # plt.ylim(X2.min(), X2.max())
# # # for i, j in enumerate(np.unique(y_pred)):
# # #    plt.scatter(X_set[y_set == j, 0], X_train.iloc[:, 3][y_set == j, 1],
# # #                c = ListedColormap(('red', 'green'))(i), label = j)
# # plt.scatter(X_test.iloc[:,0], X_test.iloc[:, 3], alpha=0.5, edgecolors='none')
# # plt.title('Test')
# # plt.xlabel('SSIP')
# # plt.ylabel('SFE')
# # plt.grid(True)
# # plt.legend()
# # plt.show()

# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np


# labels = ['SSIP', 'SDFP', 'SDFB', 'SFE', 'RFIP']
# men_means = [20, 34, 30, 35, 27]
# women_means = [25, 32, 34, 20, 25]

# x = np.arange(len(labels))  # the label locations
# width = 0.35  # the width of the bars

# fig, ax = plt.subplots()
# rects1 = ax.bar(x - width/2, men_means, width, label='Normal')
# rects2 = ax.bar(x + width/2, women_means, width, label='Anomaly')
# # rects = ax.bar(x + width/2, women_means, width, label='Women')

# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
# ax.set_xticks(x)
# ax.set_xticklabels(labels)
# # ax.legend()


# def autolabel(rects):
#     """Attach a text label above each bar in *rects*, displaying its height."""
#     for rect in rects:
#         height = rect.get_height()
#         ax.annotate('{}'.format(height),
#                     xy=(rect.get_x() + rect.get_width() / 2, height),
#                     xytext=(0, 3),  # 3 points vertical offset
#                     textcoords="offset points",
#                     ha='center', va='bottom')


# autolabel(rects1)
# autolabel(rects2)

# fig.tight_layout()

# plt.show()


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.utils.multiclass import unique_labels
import pandas as pd

# Import the dataset
df = pd.read_csv('data/dataset.csv')

# Splitting dataset into features and label
X = df.drop('Class', axis=1)
y = df['Class']

# Splitting the dataset into the training set and the test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

class_names = np.array(['Normal', 'Anomaly'])

# Run classifier, using a model that is too regularized (C too low) to see
# the impact on the results
classifier = svm.SVC(kernel='linear', random_state=0)
# classifier = LogisticRegression()
y_pred = classifier.fit(X_train, y_train).predict(X_test)

print(len(X_test))
print(classification_report(y_test, y_pred))

def plot_confusion_matrix(y_true, y_pred, classes,
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    # Only use the labels that appear in the data
    classes = classes[unique_labels(y_true, y_pred)]
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    plt.xlim(-0.5, len(np.unique(y))-0.5)
    plt.ylim(len(np.unique(y))-0.5, -0.5)
    return ax


np.set_printoptions(precision=2)

# Plot non-normalized confusion matrix
plot_confusion_matrix(y_test, y_pred, classes=class_names,
                      title='Confusion matrix, without normalization')

# plt.show()
plt.savefig('cm.png')

# Plot normalized confusion matrix
# plot_confusion_matrix(y_test, y_pred, classes=class_names, normalize=True,
                    #   title='Normalized confusion matrix')
