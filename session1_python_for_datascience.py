# >>>>>>>>>>>>>>>>>>> PYTHON FOR DATA SCIENCE <<<<<<<<<<<<<<<<<<<<<<< #

#--------------------------Pandas--------------------------------

#A series is used to model one dimensional data
# similar to a list in python
# The Series object also has a few more bits
# of data, including #index and a name.

import pandas as pd
songs2 = pd.Series([145,142,38,13], name='counts')
#It is easy to inspect the index of a series (or data)
songs2.index

#The index can be string based as well,
#in which case pandas indicates
#that the datatype for the index is object (not string )

import pandas as pd
songs3 = pd.Series([145,142,38,13],name='counts',
                   index=['paul','john','george','ringo'])
songs3.index
songs3

#The NaN value
#This value stands for Not A Number,
#and is usually ignored in arithmetic
#operations. (Similar to NULL in SQL)
#If you load data from a CSV file
#an empty value for an otherwise

#numeric column will become NaN.
#to read excel file(csv) then use read func
import pandas as pd
s1=pd.read_csv('age.csv')
s1

df=pd.read_excel('c:/1- Python/Bahaman.xlsx')

#None, Nan, nan, and null are synonyms
# The Series object behaves similarly to
# a Numpy array

import numpy as np
numpy_ser = pd.array([145,142,38,13])
songs3[1]  #accessing series element
#142
#They 
numpy_ser[1]
#They both have methods in common
songs3.mean()
numpy_ser.mean()

#############################################################
#THE PANDAS SERIES DATA STRUCTURE PROVIDES
# Support for the basic CRUD
# operations-create, read, update, and delete
# creation

george=pd.Series([10,7,1,22], index=['1968','1969','1970','1970'],
                    name='george songs')
george


""" The previous example illustrate an interesting feature of pandas-
    the index values are strings and they are not unique. This can 
    cause some confusion, but can also be useful when duplicate index items
    are needed
"""
########################################################

#Reading
#To read or select the data from a Series
george['1968']

george['1970']

#we can iterate over dat in a series
#as well. when iterating over a series
#iterating over series
for item in george:
    print(item)
######################################################
#updating
#updating values in a series can be a
#little tricky as well
#To update a value
#for a given index label,
#the standard index assignment operation 
#works
george['1968']=44
george['1968']

#deletion
# the del statement appears to have
#problems with duplicate indexS
s=pd.Series([2,3,4],index=[1,2,3])
del s[1]
s

############################################################
#convert Types
#string use.astype(str)
#numeric use pd.to_numeric
#integer use .astype(int)
#note that this will fail with NaN
#datetime use pd.to_datetime

songs_66 = pd.Series([3,None,11,9], index=['george','ringo','john','paul'],
                        name='counts')
songs_66.dtypes
#dtypes('floats64')
pd.to_numeric(songs_66.apply(str))
#There will be error
pd.to_numeric(songs_66.astype(str), errors='coerce')
#If we pass errors='coerce'
#we can see that it supports many formats
songs_66.dtypes

#Dealing with None
#The .fillna methon will replace them with a given value
songs_66.fillna(-1)

#NaN values can be dropped from 
# the series using dropna
songs_66.dropna()

####################################################
#Append, combining , and joining two series

songs_69=pd.Series([17,16,21,39],
                   index=['Ram','Sham','Ghansham','krishna'],
                   name='counts')
songs=songs_66.append(songs_69)
songs
#serie is added to the last of the first series

#################################################################

#plotting two series
import matplotlib.pyplot as plt
#plt.figure() create a figure object
fig=plt.figure()
songs_69.plot()
plt.legend()
# A legend is an area describing the elements of the graph

#######################################################

#bar graph
fig = plt.figure()
#plt.figure() create a figure object
songs_69.plot(kind='bar')
songs_66.plot(kind='bar', color='r')
plt.legend()

############################################################

import numpy as np 
data = pd.Series(np.random.randn(500),name='500 random')
fig = plt.figure()
ax = fig.add_subplot(111)
data.hist()
#########################################################





