# What is Pandas Dataframe?

""" Pandas Dataframe is Two - Dimensional data structure, 
an immutable, heterogenous tabular
Supports heterogenous collections of Data
"""
#to upgrade pandas command:
#conda install -c anaconda pandas

#upgrade to specific version
#conda update pandas==1.5.3

################################################################
#To check the version of pandas
import pandas as pd
pd.__version__

######################################################
# Create using constructor 
# create pandas Dataframe from List

import pandas as pd
technologies = [["spark",20000,"30days"], #techonologies-> List of list
                ["pandas",20000,"40days"]]
df=pd.DataFrame(technologies)
print(df)

#Since we have not given labels to columns and 
#indexes, DataFrame by default assigns
#incremental sequence numbers as labels
#to both row and columns,there are called Index.
#Add column & Row labels to the DataFrame

column_names=["courses","fee","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)

df.dtypes

#####################################################################
#You can also assign custom
# data types to colums.
#set custom types to DataFrame

import pandas as pd
technologies={ 'Courses':['Spark','Pyspark','Hadoop','Pandas','Oracle','java','c++'],
               'Fees':[20000,25000,26000,22000,24000,21000, 22000],
               'Duration':['30day','40days','35days','40days','60days','50days','55days'],
               'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]}
df=pd.DataFrame(technologies)
print(df.dtypes)
#Convert all types to best possible types
df2=df.convert_dtypes()
print(df2.dtypes)
# change all columns to same type
df = df.astype(str)
print(df.dtypes)
#Change type for one or multiple columns
df = df.astype({"Fees":int, "Discount":float})
print(df.dtypes)
#convert Data type for all columns in a list
df=pd.DataFrame(technologies)
df.dtypes
cols = ['Fees','Discount']
df[cols] = df[cols].astype('float')
df.dtypes
 
#Ignore error
df = df.astype({"Courses":int},errors='ignore')
df.dtypes

#Generates Error
df = df.astype({"Courses":int},errors='raise')
df.dtypes

#######################################################################


