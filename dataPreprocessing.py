import numpy as nm
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import zscore

#reads and copies the data from the csv file
data = pd.read_csv('/Users/alicialuna/csc177-group-project copy/uci_heartDisease_changed.csv',)
#prints out original data
print('Number of instances = %d' % (data.shape[0]))
print('Number of attributes = %d\n' % (data.shape[1]))
print(data)
#------------------------------------------------------------------------------------------
#detects duplicated data and deletes it in another copy of data
dups = data.duplicated()
print('Number of duplicate rows = %d' % (dups.sum()))
print('Now discarding duplicate rows')
data2 = data.drop_duplicates()
print('Number of instances = %d\n' % (data2.shape[0]))
print(data2)
#------------------------------------------------------------------------------------------
#Changes the missing values
data3 = data2.replace('?',nm.NaN)
print(data3)

#Counts number of missing values
print('Number of missing values:')
for col in data3.columns:
    print('\t%s: %d' % (col,data3[col].isna().sum()))

#Fills in missing values with the median of the columns
print('\nLet us fill in the missing values')
for col in data3.columns:
    column = '%s' % col
    datacol = data3[column]
    data3[column] = datacol.fillna(datacol.median())

#Recounts missing values and prints new dataset
print('\nNumber of missing values:')
for col in data3.columns:
    print('\t%s: %d' % (col,data3[col].isna().sum()))
print(data3)
#------------------------------------------------------------------------------------------
#Finding outliers
for col in data3.columns:
    column = '%s' % col
    datacol = data3[column]
    data3[column] = pd.to_numeric(data3[column])
data3.boxplot(figsize=(20,3))
plt.show()

#calculate z scores to delete outliers
Z = (data3-data3.mean())/data3.std()
print('Number of rows before discarding outliers = %d' %(Z.shape[0]))
Z2 = Z.loc[((Z > -3).sum(axis=1)==14) & ((Z <= 3).sum(axis=1)==14),:]
print('Number of rows after discarding outlier values = %d' % (Z2.shape[0]))
print(Z2)