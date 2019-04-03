import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv("iris.data")
print df.head()
print df.info()
print df.describe()
print df["sepal_length"]
print df[["sepal_length","petal_length"]]

print df.columns.values
for col in df.columns.values[:-1]:
	print col
	df.hist(column=col)
  # plt.show()
#df.boxplot((column="sepal_length","sepal_width","petal_length","petal_width"))
plt.show()

df.boxplot(column=list(df.columns.values[:-1]))

#df.hist(column="sepal_length")
plt.show()
#df.hist(column="sepal_width")
#plt.show()
#df.hist(column="petal_length")
#plt.show()
#df.hist(column="petal_width")
#plt.show()


#sudo apt-get install python-dev
#sudo apt-get install python-pip


#gescoe@gescoe-X553SA:~$ cd Desktop
#gescoe@gescoe-X553SA:~/Desktop$ cd p1
# gescoe@gescoe-X553SA:~/Desktop/p1$ python prac1.py
#    sepal_length  sepal_width  petal_length  petal_width        class
# 0           5.1          3.5           1.4          0.2  Iris-setosa
# 1           4.9          3.0           1.4          0.2  Iris-setosa
# 2           4.7          3.2           1.3          0.2  Iris-setosa
# 3           4.6          3.1           1.5          0.2  Iris-setosa
# 4           5.0          3.6           1.4          0.2  Iris-setosa
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 150 entries, 0 to 149
# Data columns (total 5 columns):
# sepal_length    150 non-null float64
# sepal_width     150 non-null float64
# petal_length    150 non-null float64
# petal_width     150 non-null float64
# class           150 non-null object
# dtypes: float64(4), object(1)
# memory usage: 7.0+ KB
# None
#        sepal_length  sepal_width  petal_length  petal_width
# count    150.000000   150.000000    150.000000   150.000000
# mean       5.843333     3.054000      3.758667     1.198667
# std        0.828066     0.433594      1.764420     0.763161
# min        4.300000     2.000000      1.000000     0.100000
# 25%        5.100000     2.800000      1.600000     0.300000
# 50%        5.800000     3.000000      4.350000     1.300000
# 75%        6.400000     3.300000      5.100000     1.800000
# max        7.900000     4.400000      6.900000     2.500000
# 0      5.1
# 1      4.9
# 2      4.7
# 3      4.6
# 4      5.0
# 5      5.4
# 6      4.6
# 7      5.0
# 8      4.4
# 9      4.9
# 10     5.4
# 11     4.8
# 12     4.8
# 13     4.3
# 14     5.8
# 15     5.7
# 16     5.4
# 17     5.1
# 18     5.7
# 19     5.1
# 20     5.4
# 21     5.1
# 22     4.6
# 23     5.1
# 24     4.8
# 25     5.0
# 26     5.0
# 27     5.2
# 28     5.2
# 29     4.7
#       ... 
# 120    6.9
# 121    5.6
# 122    7.7
# 123    6.3
# 124    6.7
# 125    7.2
# 126    6.2
# 127    6.1
# 128    6.4
# 129    7.2
# 130    7.4
# 131    7.9
# 132    6.4
# 133    6.3
# 134    6.1
# 135    7.7
# 136    6.3
# 137    6.4
# 138    6.0
# 139    6.9
# 140    6.7
# 141    6.9
# 142    5.8
# 143    6.8
# 144    6.7
# 145    6.7
# 146    6.3
# 147    6.5
# 148    6.2
# 149    5.9
# Name: sepal_length, dtype: float64
#      sepal_length  petal_length
# 0             5.1           1.4
# 1             4.9           1.4
# 2             4.7           1.3
# 3             4.6           1.5
# 4             5.0           1.4
# 5             5.4           1.7
# 6             4.6           1.4
# 7             5.0           1.5
# 8             4.4           1.4
# 9             4.9           1.5
# 10            5.4           1.5
# 11            4.8           1.6
# 12            4.8           1.4
# 13            4.3           1.1
# 14            5.8           1.2
# 15            5.7           1.5
# 16            5.4           1.3
# 17            5.1           1.4
# 18            5.7           1.7
# 19            5.1           1.5
# 20            5.4           1.7
# 21            5.1           1.5
# 22            4.6           1.0
# 23            5.1           1.7
# 24            4.8           1.9
# 25            5.0           1.6
# 26            5.0           1.6
# 27            5.2           1.5
# 28            5.2           1.4
# 29            4.7           1.6
# ..            ...           ...
# 120           6.9           5.7
# 121           5.6           4.9
# 122           7.7           6.7
# 123           6.3           4.9
# 124           6.7           5.7
# 125           7.2           6.0
# 126           6.2           4.8
# 127           6.1           4.9
# 128           6.4           5.6
# 129           7.2           5.8
# 130           7.4           6.1
# 131           7.9           6.4
# 132           6.4           5.6
# 133           6.3           5.1
# 134           6.1           5.6
# 135           7.7           6.1
# 136           6.3           5.6
# 137           6.4           5.5
# 138           6.0           4.8
# 139           6.9           5.4
# 140           6.7           5.6
# 141           6.9           5.1
# 142           5.8           5.1
# 143           6.8           5.9
# 144           6.7           5.7
# 145           6.7           5.2
# 146           6.3           5.0
# 147           6.5           5.2
# 148           6.2           5.4
# 149           5.9           5.1

# [150 rows x 2 columns]
# ['sepal_length' 'sepal_width' 'petal_length' 'petal_width' 'class']
# sepal_length
# sepal_width
# petal_length
# petal_width
# prac1.py:18: FutureWarning: 
# The default value for 'return_type' will change to 'axes' in a future release.
#  To use the future behavior now, set return_type='axes'.
#  To keep the previous behavior and silence this warning, set return_type='dict'.
#   df.boxplot(column=list(df.columns.values[:-1]))
# gescoe@gescoe-X553SA:~/Desktop/p1$ 
