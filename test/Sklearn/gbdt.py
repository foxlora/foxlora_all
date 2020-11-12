from sklearn import datasets

import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

#加载数据
train = pd.read_csv('train_modified.csv')
target='Disbursed' # Disbursed的值就是二元分类的输出
IDcol = 'ID'




x_columns = [x for x in train.columns if x not in [target, IDcol]]
X = train[x_columns]
y = train['Disbursed']

# lr = LogisticRegression()
# lr.fit(X,y)
# y_pred = lr.predict(X)
# y_predprob = lr.predict_proba(X)[:,1]
#
# print(y_pred)
# print(y_predprob)
gbm = GradientBoostingClassifier()
gbm.fit(X,y)

y_pred = gbm.predict(X)
y_predprob = gbm.predict_proba(X)[:,1]


print("Accuracy : %.4g" % metrics.accuracy_score(y.values, y_pred))
print("AUC Score (Train): %f" % metrics.roc_auc_score(y, y_predprob))



