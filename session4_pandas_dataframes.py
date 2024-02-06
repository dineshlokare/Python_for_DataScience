import pandas as pd
technologies={ 'Courses':['Spark','Pyspark','Hadoop','Pandas','Oracle','java','c++'],
               'Fees':[20000,25000,26000,22000,24000,21000, 22000],
               'Duration':['30day','40days','35days','40days','60days','50days','55days'],
               'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]}
df=pd.DataFrame(technologies)
print(df.dtypes)

##########################################################

#convert dataframe to csv
df.to_csv('data_file.csv')

#create dataframe from csv file
df = pd.DataFrame('data_file.csv')

#create dataframe from csv file
df = pd.read_csv('data_file.csv')

###########################################################################

import pandas as pd
import numpy as np
technologies={ 'Courses':['Spark','Pyspark','Hadoop','Pandas','Oracle','java','c++'],
               'Fees':[20000,25000,26000,22000,24000,21000, 22000],
               'Duration':['30day','40days','35days','40days',' ','50days','55days'],
               'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]}
row_labels=['r0','r1','r2','r3','r4','r5','r6']
df = pd.DataFrame(technologies,index=row_labels)
print(df)

####################################
#Dataframe properties
df.shape
#(7,4)
df.size
#28
df.columns
df.columns.values
df.index
df.dtypes

##################################################
#Acessing one column contents
df['Fees']
#Acessing two columns contents
df[["Fees","Duration"]]
#Select certain rows and assign it to another dataframe
df2=df[6:]
df2

#################################################
#Accessing certain cell from column'Duration'
df['Duration'][3]
#substracting specific value from a column
df['Fees'] = df['Fees'] - 500
df['Fees']

#Pandas to Manipulate Dataframe 
#Describe Dataframe
#Describing dataframe for all numeric columns
df.describe()
#It will show 5 number summary
###########################################################

#rename() - Renames pandas DataFrame columns
df = pd.DataFrame(technologies,index=row_labels)

#Assign new header by setting new column names.
df.columns=['A','B','C','D']
df 


################################################################
# Rename column names using rename() method

df=pd.DataFrame(technologies, index=row_labels)
df.columns=['A','B','C','D']
df2 = df.rename({'A':'c1','B':'c2'}, axis=1)
df2
df2 = df.rename({'C':'c3','D':'c4'}, axis='columns')
df2
df2 = df.rename(columns={'A':'c1','B':'c2'})
df2
df
