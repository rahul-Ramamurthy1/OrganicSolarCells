import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor




data = pd.read_csv("C:\\Users\\rahul\\Downloads\\RahulRSMDM.csv")

data['S'] = ''
data['N'] = ''
data['Se'] = ''
data['O'] = ''
data['F'] = ''
data['H'] = ''
data['P'] = ''
data['C'] = ''
data['Cl'] = ''
data['Br'] = ''



for i in range(0,49):
    temp = re.findall(r'\d+', data["Chemical Composition"][i])
    res = list(map(int, temp))
    np.asarray(res)
    data["Chemical Composition"][i] = res
    #print(res[9])
    data['S'][i] = res[0]
    data['N'][i] = res[1]
    data['Se'][i] = res[2]
    data['O'][i] = res[3]
    data['F'][i] = res[4]
    data['H'][i] = res[5]
    data['P'][i] = res[6]
    data['C'][i] = res[7]
    data['Cl'][i] = res[8]


data['Br'] = 0
data['Br'][34] = 2
del data['Chemical Composition']
#print(data['FF'].mean(),data['FF'].std())


#Data Preparation
X = data[['HOMO Level','LUMO Level','S','N','Se','O','F','H','P','C','Cl','Br']]
y = data['FF']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)


#Lin Reg
'''regr = linear_model.LinearRegression()
regr.fit(X_train, y_train)
y_pred = regr.predict(X_test)
print(y_pred)
print(metrics.mean_squared_error(y_pred,y_test))
print(metrics.mean_absolute_error(y_pred,y_test))'''

#Random Forest
mae_values = []
for i in range(10,101,10):
    regr2 = RandomForestRegressor(max_depth=None,random_state=0,n_estimators=i)
    regr2.fit(X_train, y_train)
    y_pred = regr2.predict(X_test)
    #print(y_pred)
    #print(metrics.mean_squared_error(y_pred,y_test))
    #print(metrics.mean_absolute_error(y_pred,y_test))
    mae_values.append(metrics.mean_absolute_error(y_pred,y_test))

plt.plot(range(10,101,10),mae_values)
plt.show()

#n_estimators = 80, max_depth = 3
