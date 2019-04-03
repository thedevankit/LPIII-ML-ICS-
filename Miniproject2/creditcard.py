import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pprint
sns.set()

import os

data = pd.read_csv('creditcard.csv')

data.head()

features = data.columns[:-1]
print('The features are as follows: {}'.format(features))
target = data.columns[-1]
print('The target is: ' + target)

X = data[features]
y = data[target]

X.hist(figsize = (20, 20))
plt.show()

count_target = pd.value_counts(y, sort = True).sort_index()
count_target.plot(kind = 'bar')
plt.xticks(rotation=0)
plt.title("Fraud class histogram")
plt.xlabel("Class")
plt.ylabel("Frequency")
plt.show()


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# Scale `Amount` and `Time` column values and assign to new columns
X['normAmount'] = scaler.fit_transform(X['Amount'].values.reshape(-1, 1)) 
X['normTime'] = scaler.fit_transform(X['Time'].values.reshape(-1, 1))

# Drop pre-scaled `Time` and `Amount` values from the feature dataset
X = X.drop(['Time','Amount'],axis=1)

# Plot histograms of each parameter 
X.hist(figsize = (20, 20))
plt.show()


from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,precision_recall_curve,auc,roc_auc_score,roc_curve,recall_score,classification_report 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Instantiate the model
from sklearn.linear_model import LogisticRegression
lg_model = LogisticRegression(solver = 'liblinear')

# Train the model using 'fit' method
lg_model.fit(X_train, y_train)

# Test the model using 'predict' method
y_pred = lg_model.predict(X_test)

# Print the classification report 
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test,y_pred)

# print confusion matrix
ax= plt.subplot()
sns.heatmap(cm, annot=True, fmt = 'd', ax = ax); #annot=True to annotate cells

# labels, title and ticks
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Logistic regression: Confusion Matrix'); 
ax.xaxis.set_ticklabels(['Non-fradulent', 'Fradulent']); ax.yaxis.set_ticklabels(['Non-fradulent', 'Fradulent']);

lg_model_accuracy = lg_model.score(X_test, y_test)
print("Model accuracy: ", lg_model_accuracy)



y_pred_prob = lg_model.predict_proba(X_test)[:,1]
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
plt.plot([0, 1], [0, 1], linestyle='--')
plt.plot(fpr, tpr, label='Logistic Regression')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title('Logistic Regression ROC Curve')
plt.show()

print('The ROC AUC score is: {}'.format(roc_auc_score(y_test, y_pred_prob)))

#Area Under the Precision-Recall Curve (AUPRC)
precision, recall, thresholds = precision_recall_curve(y_test, y_pred_prob)
# Plot comparison to no-skill model
plt.plot([0, 1], [0.5, 0.5], linestyle='--', label='Unskilled model')
# plot the roc curve for the model
plt.plot(recall, precision, marker='.')
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title('Logistic Regression Precision-Recall Curve')
# show the plot
plt.show()



from sklearn.model_selection import cross_val_score

# Number of data points in the minority class
number_records_fraud = len(y[y.values == 1])
fraud_indices = np.array(y[y.values == 1].index)

# Picking the indices of the normal classes
normal_indices = y[y.values == 0].index

# Out of the indices we picked, randomly select an x number (== number_records_fraud)
random_normal_indices = np.random.choice(normal_indices, number_records_fraud, replace = False)
random_normal_indices = np.array(random_normal_indices)

# Appending the 2 indices
under_sample_indices = np.concatenate([fraud_indices,random_normal_indices])

# Under sample dataset
under_sample_data = data.iloc[under_sample_indices,:]

#X_undersample = under_sample_data.ix[:, under_sample_data.columns != 'Class']
#y_undersample = under_sample_data.ix[:, under_sample_data.columns == 'Class']


# Under sample dataset
X_undersample = X.iloc[under_sample_indices,:]
y_undersample = y.iloc[under_sample_indices]

# Showing ratio
print("Percentage of normal transactions: ", len(under_sample_data[under_sample_data.Class == 0])/len(under_sample_data))
print("Percentage of fraud transactions: ", len(under_sample_data[under_sample_data.Class == 1])/len(under_sample_data))
print("Total number of transactions in resampled data: ", len(under_sample_data))

# Undersampled dataset
X_train_undersample, X_test_undersample, y_train_undersample, y_test_undersample = train_test_split(X_undersample
                                                                                                   ,y_undersample
                                                                                                   ,test_size = 0.3
                                                                                                   ,random_state = 1)
print("")
print("Number transactions training dataset: ", len(X_train_undersample))
print("Number transactions test dataset: ", len(X_test_undersample))
print("Total number of transactions: ", len(X_train_undersample)+len(X_test_undersample))

# Instantiate the model
from sklearn.linear_model import LogisticRegression
lg_model = LogisticRegression(solver = 'liblinear')

# Train the model using 'fit' method
lg_model.fit(X_train_undersample, y_train_undersample)

# Test the model using 'predict' method
y_pred_undersample = lg_model.predict(X_test_undersample)

# Print the classification report 
print(classification_report(y_test_undersample, y_pred_undersample))

cm_undersample = confusion_matrix(y_test_undersample,y_pred_undersample)

# print confusion matrix
ax= plt.subplot()
sns.heatmap(cm_undersample, annot=True, fmt = 'd', ax = ax); #annot=True to annotate cells

# labels, title and ticks
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Logistic regression: Confusion Matrix'); 
ax.xaxis.set_ticklabels(['Non-fradulent', 'Fradulent']); ax.yaxis.set_ticklabels(['Non-fradulent', 'Fradulent']);

lg_model_accuracy_undersample = lg_model.score(X_test_undersample, y_test_undersample)
print("Model accuracy: ", lg_model_accuracy_undersample)


#cv_scores = cross_val_score(lg_model, X, y, cv=5, scoring='roc_auc')
#print("The scores of 5-fold cross-validation are: {}".format(cv_scores))
#print("The mean cross-validation score is: {}".format(np.mean(cv_scores)))

y_pred_prob_undersample = lg_model.predict_proba(X_test_undersample)[:,1]
fpr, tpr, thresholds = roc_curve(y_test_undersample, y_pred_prob_undersample)
plt.plot([0, 1], [0, 1], linestyle='--')
plt.plot(fpr, tpr, label='Logistic Regression')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title('Logistic Regression ROC Curve')
plt.show()

print('The ROC AUC score is: {}'.format(roc_auc_score(y_test_undersample, y_pred_prob_undersample)))

#Area Under the Precision-Recall Curve (AUPRC)
precision, recall, thresholds = precision_recall_curve(y_test_undersample, y_pred_prob_undersample)
# Plot comparison to no-skill model
plt.plot([0, 1], [0.5, 0.5], linestyle='--', label='Unskilled model')
# plot the roc curve for the model
plt.plot(recall, precision, marker='.')
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title('Logistic Regression Precision-Recall Curve')
# show the plot
plt.show()