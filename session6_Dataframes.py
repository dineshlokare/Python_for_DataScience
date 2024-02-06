
import pandas as pd
import numpy as np
technologies={ 'Courses':['Spark','Pyspark','Hadoop','Pandas','Oracle','java','c++'],
               'Fees':[20000,25000,26000,22000,24000,21000, 22000],
               'Duration':['30day','40days','35days','40days',' ','50days','55days'],
               'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]}
row_labels=['r0','r1','r2','r3','r4','r5','r6']
df = pd.DataFrame(technologies,index=row_labels)
print(df)


df=pd.DataFrame(technologies, index=row_labels)
df.columns=['A','B','C','D']
df2 = df.rename({'A':'c1','B':'c2'}, axis=1)
df2
df2 = df.rename({'C':'c3','D':'c4'}, axis='columns')
df2
df2 = df.rename(columns={'A':'c1','B':'c2'})
df2
df

############################################################
#Drop DataFrame Rows and Columns

df = pd.DataFrame(technologies, index=row_labels)
df

# Drop rows by labels

df = df.drop(['r1','r2'])
df

#Delete rows by position/index

df = df.drop(df.index[1])
df
df = df.drop(df.index[[1,3]])
df
#delete rows by index range

df=df.drop(df.index[2:])
df

#When you have default indexs for rows

df=pd.DataFrame(technologies)
df1 = df.drop(0)
df1

df = pd.DataFrame(technologies)
df1 = df.drop([0,3]) #It will delete row0 and row3
df1
df1 = df.drop(range(3,5)) # it will delete 3 and 4
df1

#Dropping of columns 

import pandas as pd
import numpy as np
technologies={ 'Courses':['Spark','Pyspark','Hadoop','Pandas','Oracle','java','c++'],
               'Fees':[20000,25000,26000,22000,24000,21000, 22000],
               'Duration':['30day','40days','35days','40days',' ','50days','55days'],
               'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]}
df = pd.DataFrame(technologies)
print(df)

#Drop column by Name
#Drop 'Fees' column
#it is mandatory to write axis=1 when dropping with column

df2 = df.drop(['Fees'],axis=1)
df2

#another way of dropping columns
#Explicitly using paramete name 'labels'

df2 = df.drop(labels=['Courses'],axis=1)
df2

#Alternately you can also use columns instead of label
df2 = df.drop(columns=['Duration'],axis=1)
df2

############################################################
# Drop column by index
df
print(df.drop(df.columns[1],axis=1))
df

# using inplace=True
# when working on original dataframe it is mandatory to use inplace

df.drop(df.columns[2],axis=1,inplace=True)
print(df)

######################################################

df = pd.DataFrame(technologies)

#Drop Two or More columns By label Name
df2=df.drop(['Courses','Fees'],axis=1)
print(df2)

#################################################################

#Drop two or more columns by index

df =pd.DataFrame(technologies)
print(df)

df2 = df.drop(df.columns[[0,1]],axis=1)
print(df2)

#######################################################
#Drop columns from list of columns

df = pd.DataFrame(technologies)
df.columns
lisCol = ['Courses','Fees']
df2=df.drop(lisCol, axis=1)
print(df2)
df2.columns
#lisCol is used to drop columns from the list of columns
#used in industry people most of the time

#######################################################
#slicing specific rows and columns from DataFrame

#loc
#iloc
#df.iloc[startrow:endrow, startcolumn:endcolumn]

df=pd.DataFrame(technologies)
print(df)

#Below are quick example

s=df.iloc[:,0:2]
s

#This line uses the slicing to get DataFrame
# Items by Index.
# The first slice[:] indicates to return all rows
# The second slice specifies that only columns 
# between 0 and 2 (excluding 2) should be returned

s = df.iloc[0:2,:]
s

#In this the first slice [0:2] is 
# requesting only rows 0 through 1 of the DataFrame
# The second slice [:] indicattes that all columns are request

#Slicing specific rows and columns using iloc 

df = pd.DataFrame(technologies)
df

s1 = df.iloc[1:2,1:3]
s1

# another example
s2 = df.iloc[:,1:3]
s2

#select rows by integer index
s = df.iloc[2] #select row by index
s

df=pd.DataFrame(technologies)
print(df)

v = df.iloc[[2,3,6]]  #select rows by index
v
v = df.iloc[1:5]    #select rows by integer index range
v
v = df.iloc[:1]     #select first row
v
v = df.iloc[:3]     #select first 3 rows
v
v = df.iloc[-1:]    #select last row
v
v = df.iloc[-3:]    #select last 3 rows
v
v = df.iloc[::2]     #select alternate rows
v


# select rows by Index labels

import pandas as pd
import numpy as np
technologies={ 'Courses':['Spark','Pyspark','Hadoop','Pandas','Oracle','java','c++'],
               'Fees':[20000,25000,26000,22000,24000,21000, 22000],
               'Duration':['30day','40days','35days','40days',' ','50days','55days'],
               'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]}
row_labels=['r0','r1','r2','r3','r4','r5','r6']
df = pd.DataFrame(technologies,index=row_labels)
print(df)

t = df.loc['r2']        #Select row by label
t
t = df.loc[['r2','r3','r6']] #slect rows by index label
t = df.loc['r1':'r5'] # select rows by index label
t
t = df.loc['r1':'r5':2] # select alternate rows by index label
t
#in index with range [1:4] excluding 4 row but with
#index label [1:4] it will include 4th row also

#########################################################
#slices of columns
#Pandas select columns by Name or Index

# By using df[] Notation
df = pd.DataFrame(technologies)
df

#select multiple columns
df2 = df[['Courses','Fees','Duration']]
df2

#Using loc[] to take column slices
#loc[] syntax to slice columns
#df.loc[:,start:stop:step]
#selected multiple columns

df2 = df.loc[:,["Courses","Fees","Duration"]]
df2
#Select random columns
df2 = df.loc[:,["Courses","Fees","Discount"]]
df2
#select columns between two columns
df2 = df.loc[:,'Fees':'Discount']
df2
#slect columns by range
df2 = df.loc[:,'Duration']
df2
#Select columns by range
#All columns upto 'Duration'
df2=df.loc[:,:'Duration']
df2




