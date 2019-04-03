import pandas as pd
import numpy as np

#reading Dataset
dataset=pd.read_csv("data.csv")
X=dataset.iloc[:,:-1]
y=dataset.iloc[:,5]

#Perform Label encoding
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

X=X.apply(le.fit_transform)
print("X")

from sklearn.tree import DecisionTreeClassifier
regressor=DecisionTreeClassifier()
regressor.fit(X.iloc[:,1:5],y)

#Predict value for the given Expression
X_in=np.array([1,1,0,0])
y_pred=regressor.predict([X_in])
print("Prediction:", y_pred)
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus

dot_data=StringIO()

export_graphviz(regressor,out_file=dot_data,filled=True,rounded=True,special_characters=True)
graph=pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('tree.png')


####################OUTPUT##################################################
#sudo apt-get install python-pydot
#sudo apt install ipython
# chanchald@chanchald-X553SA:~/Desktop/ml/ML2$ python ml2.py
# X
# ('Prediction:', array(['Yes'], dtype=object))
# chanchald@chanchald-X553SA:~/Desktop/ml/ML2$ 