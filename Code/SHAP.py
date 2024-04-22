import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Load Data
#APPAC, PAAC, AAC, & DPC
X1=pd.read_csv('Features/Sodium_APAAC.csv', header=None).iloc[:,1:].values
X2=pd.read_csv('Features/Sodium_PAAC.csv', header=None).iloc[:,1:].values
X3=pd.read_csv('Features/Sodium_AAC.csv', header=None).iloc[:,1:].values
X4=pd.read_csv('Features/Sodium_DPC.csv', header=None).iloc[:,1:].values
X=np.concatenate((X1,X2, X3, X4), axis=1, out=None)

#Labels
pos_labels = np.ones(492)
neg_labels = np.zeros(492)
y = np.concatenate((pos_labels,neg_labels),axis=0)

#Split X 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.2, random_state=67, stratify=y)

#Load Model
model = pickle.load(open('NaII-Pred.pkl', 'rb'))

#SHAP
import shap
explainer = shap.Explainer(model.predict, X_train)
shap_values = explainer.shap_values(X_test)

fig = plt.figure(figsize=(8,8))
fig.set_facecolor('white')
ax = fig.add_subplot()
shap.summary_plot(shap_values, df, max_display=10, show=False)
ax.set_xlabel('SHAP Value (imapct on model output)', fontsize=14)
ax.tick_params(axis='x', labelsize=13, length=7)  # adjust x-axis tick labels font size
ax.tick_params(axis='y', labelsize=13, length=7)  # adjust y-axis tick labels font size
#plt.savefig('SHAP_test.jpg', bbox_inches='tight', dpi=600)
