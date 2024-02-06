###############################################
########################################

import pandas as pd
import numpy as np
technologies={ 'Courses':['Spark','Pyspark','Hadoop','Pandas','Oracle','java','c++'],
               'Fees':[20000,25000,26000,22000,24000,21000, 22000],
               'Duration':['30days','40days','35days','40days',' ','50days','55days'],
               'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
             }
row_labels=['r0','r1','r2','r3','r4','r5','r6']
df = pd.DataFrame(technologies,index=row_labels)
print(df)

#Pandas.Dataframe.query() by examples
#Query all rows with courses equals to 'Spark'

df2 = df.query("Courses == 'Spark'")
print(df2)

#######################################
#not equals conditin
df2 = df.query("Courses != 'Spark'")
df2

###################################################

#Pandas add column to Dataframe

df = pd.DataFrame(technologies)
df

#Add new column to Dataframe

tutors = ['Ram','Sham','Ghansham','Ganesh','Ramesh','Dinesh','Shashi']
df2 = df.assign(TutorsAssigned=tutors)
print(df2)

#########################################################

#Add multiple columns to Dataframe

MNCCompanies = ['Google','HCL','Tata','Netflix','Infosys','Amazon','Meta']
df2 = df.assign(MNC=MNCCompanies, TutorsAssigned=tutors)
print(df2)

#############################################################

#Derive new column from Existing column
#lambda function is used

df=pd.DataFrame(technologies)
df2 = df.assign(Discount_percent = lambda x: x.Fees * x.Discount / 100)
print(df2)

#imp topic

###################################################################

#Append column to existing pandas DataFrames
#Add new column to existing Dataframe

df = pd.DataFrame(technologies)
df["MNCCompanies"] = MNCCompanies
print(df)

#################################################################
#Add new column at specific position
#here column is added at the 0th position

df = pd.DataFrame(technologies)
df.insert(0,'Tutors',tutors)
print(df)

###################################################################

#Quick examples to Get the Number of Rows in DataFrame

rows_count = len(df.index)
rows_count
rows_count = len(df.axes[0])
rows_count
column_count = len(df2.axes[1])
column_count

df = pd.DataFrame(technologies)
row_count = df.shape[0]     #Returns number of rows
col_count = df.shape[1]     #Returns number of Columns
print(row_count)
print(col_count)

########################################################################




