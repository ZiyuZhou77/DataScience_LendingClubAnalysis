import pandas as pd
import numpy as np
from tpot import TPOTRegressor
from sklearn.model_selection import train_test_split

loan_data = pd.read_csv('FeatureEnggToDo.csv',error_bad_lines=False,encoding = "utf-8")
loan_data.drop(['issue_d'],axis=1,inplace=True)
labels = list(loan_data.columns.values)
print labels
data_array = np.array(loan_data)

x = data_array[:, 1:data_array.shape[1]]
y_train=x[:,2]
X_train=x[:,[v for v in range(len(x[0])) if v !=2]]


X_train, X_test, y_train, y_test = train_test_split(X_train,y_train,train_size=0.75,test_size=0.25,random_state=1)
tpot = TPOTRegressor(generations=5,population_size=20,verbosity=2)
tpot.fit(X_train, y_train)
print(tpot.score(X_test, y_test))
tpot.export('pipeline.py')


# X_train, X_test, y_train, y_test = train_test_split(X_train,y_train, test_size=0.3, random_state=0)
# tpot = TPOTClassifier(generations=5, population_size=20, verbosity=2)
# tpot.fit(X_train, y_train)
# print(tpot.score(X_test, y_test))
# tpot.export('tpot_result.py')







