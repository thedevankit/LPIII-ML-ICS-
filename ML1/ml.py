import matplotlib.pyplot as plt
import pandas as pd

# Read Dataset
dataset=pd.read_csv("hours.csv")
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values

# Import the Linear Regression and Create object of it
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X,y)
print "Accuracy :", regressor.score(X, y)*100
#print("Accuracy :")
#print(Accuracy)

# Predict the value using Regressor Object
y_pred=regressor.predict([[8]])
print(y_pred)

# Take user input
hours=int(input('Enter the no of hours:'))

#calculate the value of y
eq=regressor.coef_*hours+regressor.intercept_
print 'y = %f*%f+%f' %(regressor.coef_,hours,regressor.intercept_)
#print("y :")
#print(y)
print("Risk Score : ", eq[0])
plt.plot(X,y,'o')
plt.plot(X,regressor.predict(X));
plt.show()


#####################OUTPUT###################################
#gescoe@gescoe-X553SA:~$ cd Desktop
#gescoe@gescoe-X553SA:~/Desktop$ cd ml
#gescoe@gescoe-X553SA:~/Desktop/ml$ python ml.py
# Accuracy : 43.709481451010035
# [49.28781684]
# Enter the no of hours:10
# y = 4.587899*10.000000+12.584628
# ('Risk Score : ', 58.46361406377759)

