import pandas as pd
import numpy as np
df=pd.read_csv("iris.csv")
df

# Program to get the first three rows of a given DataFrame
df2 = df.iloc[:3]
df2


df.describe()

#Pandas.DataFrame.query()
# Query all rows with SepalLengthCm equals to 4.8
df2=df.query("sepal_length == 4.8")
print(df2)


########################

# not equals condition
df2=df.query("sepal_length!= 4.8")
df2


######################################################

# Derive new column from existing column

df2 = df.assign(Percent=lambda x: x.petal_length * x.petal_width / 100)
print(df2)


#######################################################


# Get the number of rows in DataFrame
rows_count = len(df.index)
rows_count

rows_count = len(df.axes[0])
rows_count

column_count = len(df.axes[1])
column_count

########  Another Method  ########

row_count = df.shape[0]  #Returns number of Rows
column_count = df.shape[1]   #Returns number of columns
print(row_count)
print(column_count) 

rows_count = len(df.index[0:2])
print("total number of rows: "+str(rows_count))

rows_count = len(df.axes[0])
print("total number of rows: "+str(rows_count))

###############################################################

# Program to select Id and SepalLengthCm columns from given dataframe
df2 = df.iloc[:,:2]
df2

########## Another Method #############
df2 = df.loc[:,['sepal_length','petal_length']]
df2


# Program to select the specified columns and rows from a given data
df2 = df.iloc[1:4,[1,3]]
df2

# Program to select rows where SepalWidthCm is greater than 3.2
print(df[df['sepal_length']>3.2])



# Program to select rows the SepalLengthCm is between 4.6 and 5.4
print("Rows where the SepalLengthCm is between 4.6 and 5.4: ")
print(df[df['sepal_length'].between(4.6, 5.4)])


# Program to select number of rows where the SepalLengthCm is less than 5.1 and SepalLengthCm greater than 4.8
print(df[(df['sepal_length']< 5.1) & (df['sepal_length']>4.8)])


# Program to change the PetalWidthCm in row 7 to 5
df.loc[7,'petal_width'] = 5
df


# program to calculate sum of PetalWidthCm
print(df['petal_length'].sum())


# Program to calculate mean of SepalWidthCm
print(df['sepal_width'].mean())


# Program to append new row 155 to dataframe with the given
# values for each column
df.loc[155]= [151,0.2,3.2,5.4,6.4,'Iris-setosa']
df


# program to sort the dataframe first by 'SepalLengthCm' in descending order
# then by 'PetalLengthCm' in ascending order
df=df.sort_values(by=['sepal_length'],ascending=[False])
print(df)
df = df.sort_values(by=['petal_length'],ascending=[True])
print(df)


# To replace the PetalLengthCm column contain the value 1.4 by 0.4,
# 4.6 by 4.1 and 2.8 by 2.0
df=pd.read_csv("iris.csv")
df['petal_length']=df['petal_length'].map({1.4 : 0.4, 4.6 : 4.1, 2.8 : 2.0})
df


# Program to change the name Iris-versicolor to Iris in Species
# column of the dataframe
df['species']=df['species'].replace('Iris-versicolor', 'Iris')
print(df)


# Program to iterate over rows in dataframe
for index, row in df.iterrows():
    print(row['species'],row['sepal_length'])



#--------Apply Function to Column-------#


# using DataFrame.apply() to apply function and column
df=pd.read_csv("iris.csv")
def add_4(x):
    return x+4
df2=df['petal_length'].apply(add_4)
df2


# apply to multiple column
df=pd.read_csv("iris.csv")
def add_3(x):
    return x+3
df2=df[['sepal_length','sepal_width']].apply(add_3)
df2  


# apply lambda function to specific column
df2['petal_length']=df.petal_width.apply(lambda x:x+7)
df2

# using Pandas DataFrame.map() to single column
df=pd.read_csv("iris.csv")
df['sepal_length'] = df['sepal_length'].map(lambda sepal_length : sepal_length/2)
df

# Using Numpy fuction on single column
# using DataFrame.apply() and [] operator
import numpy as np
df=pd.read_csv("iris.csv")
df['sepal_length'] = df['sepal_length'].apply(np.square)
print(df)


# Using groupby() function to sum
df=pd.read_csv("iris.csv")
df.groupby(['sepal_length']).sum()
df

# Get the list of all column names from headers
column_header = list(df.columns.values)
print(column_header)


# Pandas shuffle DataFrame Rows
df=pd.read_csv("iris.csv")
df1 = df.sample(frac = 1)
print(df1)
















