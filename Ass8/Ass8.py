from pandas import read_csv
from pandas import datetime
from pandas import DataFrame
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.arima_model import ARMA
from matplotlib import pyplot
from matplotlib import pyplot
from matplotlib.pyplot import plot
import random
from matplotlib.pyplot import figure
from math import sqrt
from multiprocessing import cpu_count
from joblib import Parallel
from joblib import delayed
from warnings import catch_warnings
from warnings import filterwarnings
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_squared_error
from pandas import read_csv
from numpy import array
import numpy as np
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder






train = read_csv("train.csv",  usecols = ['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked','Survived']) 
train = train.dropna()
ctrain = train['Survived']
train = train.drop('Survived', axis =1)
test = read_csv("test.csv",  usecols = ['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']) 


le1 = LabelEncoder()
ohe = OneHotEncoder()
le2 = LabelEncoder()


train['Sex'] = le1.fit_transform(train['Sex']) 
train['Embarked'] = le2.fit_transform(train['Embarked'])
test['Sex'] = le1.transform(test['Sex']) 
test['Embarked'] = le2.transform(test['Embarked'])
test = test.fillna(0)


clas = DecisionTreeClassifier(criterion = "entropy", random_state = 1)



clas.fit(train,ctrain)

y = read_csv("gender_submission.csv", usecols = ['Survived'])
y = np.array(y)
y = [i[0] for i in y]
y_hat = clas.predict(test)
y_hat = [i for i in y_hat]

from sklearn.metrics import confusion_matrix

c1 = confusion_matrix(y,y_hat)


acc = (c1[0][0]+c1[1][1])*100/418


print("\n\n\ngini Accuracy = ",acc, "%\n\n\n")

clas = DecisionTreeClassifier(criterion = "gini", random_state = 1)



clas.fit(train,ctrain)

y = read_csv("gender_submission.csv", usecols = ['Survived'])
y = np.array(y)
y = [i[0] for i in y]
y_hat = clas.predict(test)
y_hat = [i for i in y_hat]

from sklearn.metrics import confusion_matrix

c2 = confusion_matrix(y,y_hat)





acc = (c2[0][0]+c2[1][1])*100/418



print("\n\n\ngini Accuracy = ",acc, "%\n\n\n")






