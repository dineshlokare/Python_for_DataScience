#Pandas Apply function to a column
# Below are quick examples
# Using DataFrame.apply() to apply function and column

import pandas as pd
import numpy as np

data = {"A":[1,2,3],
        "B":[4,5,6],
        "C":[7,8,9]
        }
df = pd.DataFrame(data)
print(df.to_string)

def add_3(x):
    return x+3
df2 = df.apply(add_3)
print(df2)

#also for single column
df["A"].apply(add_3)

# also
df2 = ((df.A).apply(add_3))
df2

####################################################################
#using apply function for single column

def add_2(x):
    return x+2
df["A"]= df["A"].apply(add_2)
df["A"]

#Apply to multiple column

df[['A','C']] = df[['A','C']].apply(add_2)
print(df)

"""when you are going to apply fucntion on multiple columns then, you
    will have to pass a list
"""

#apply a lambda fucntion to each column

df2 = df.apply(lambda x: x+10)
print(df2)

#on specific column
df1 = df['A'].apply(lambda x: x + 5)
print(df1)

###############################################################3#
# Using Pandas.DataFrame.transform() to Apply function column
# using DataFrame.transform()

def add_4(x):
    return x + 4
df = df.transform(add_4)
print(df)

#######################################################################

#using Pandas.DataFrame.map() to single column

df['A'] = df['A'].map(lambda A:A/2)
df['A']

#######################################################################

#using numpy function on single column
# Using DataFrame.apply() & [] operator

import numpy as np
df['A'] = df['A'].apply(np.square)
print(df)

#######################################################################

#Using Numpy.square() method
# using numpy.square() and [] operator

df['A'] = np.square(df['A'])
print(df)

########################################################################

#Pandas groupby() with examples 

import pandas as pd
import numpy as np
technologies={ 'Courses':['Spark','Pyspark','Hadoop','Python','Pandas','Hadoop','Spark','Python','NA'],
               'Fees':[22000,25000,23000,24000,26000,25000,25000,22000,1500],
               'Duration':['30days','40days','55days','40days','60days','35days','30days','50days','40days'],
               'Discount':[1000,2300,1000,1200,2500,np.nan,1400,1600,0]
             }
df = pd.DataFrame(technologies)
print(df)

df2 = df.groupby(['Courses']).sum()
print(df2)

#For multiple columns
df2 = df.groupby(['Courses','Duration']).sum()
print(df2)

###########################################################################
#Add Index to the grouped data
# Add row Index to the group by result

df2 = df.groupby(['Courses','Duration']).sum().reset_index()
print(df2)

#######################################################################

#Pandas Get column Names from DataFrame

import pandas as pd
import numpy as np
technologies={ 'Courses':['Spark','Pyspark','Hadoop','Python','Pandas','Hadoop','Spark','Python','NA'],
               'Fees':[22000,25000,23000,24000,26000,25000,25000,22000,1500],
               'Duration':['30days','40days','55days','40days','60days','35days','30days','50days','40days'],
               'Discount':[1000,2300,1000,1200,2500,np.nan,1400,1600,0]
             }
df = pd.DataFrame(technologies)
print(df)

df.columns
df.columns.values.tolist()

#Get the list of all column names from headers
column_headers = list(df.columns.values)
print('The Column Header: ', column_headers)

############################################################################

#Pandas Shuffle DataFrame Rows 

import pandas as pd
import numpy as np
technologies={ 'Courses':['Spark','Pyspark','Hadoop','Python','Pandas','Hadoop','Spark','Python','NA'],
               'Fees':[22000,25000,23000,24000,26000,25000,25000,22000,1500],
               'Duration':['30days','40days','55days','40days','60days','35days','30days','50days','40days'],
               'Discount':[1000,2300,1000,1200,2500,np.nan,1400,1600,0]
             }
df = pd.DataFrame(technologies)
print(df)

#Pandas shuffle Dataframe Rows
# shuffle the Dataframe rows & return all rows

df1 = df.sample(frac=0.5) #only 50% will shuffle
print(df1)

df1 = df.sample(frac=1)
print(df1)          #all will shuffle


############################################################################

#create a new Index Starting from zero
df1 = df.sample(frac = 1).reset_index()
print(df1)

# if you set drop = True, reset_index will delete the index instead of
#inserting it back into the columsn of the DataFrame

df1 = df.sample(frac = 1).reset_index(drop=True)
print(df1)

#############################################################

#joins

import pandas as pd
import numpy as np
technologies1={'Courses':['Spark','Pyspark','Python','Pandas'],
               'Fees':[22000,25000,23000,24000],
               'Duration':['30days','40days','55days','40days'],
             }
index_labels1= ['r1','r2','r3','r4']
df1=pd.DataFrame(technologies1,index = index_labels1)
print(df1)

technologies2 = {'Courses': ['Spark','Java','Python','Go'],
                  'Discount':[2000,1300,2300,1200]
                  }
index_labels2 = ['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2, index = index_labels2)
print(df2)

##################################################################
#Panda inner join is mostly used join,
#It is used to join two DataFrames on indexes.
#When indexes don't match the rows get dropped from both DataFrame

###################################################################
# Pandas join, by default it will join the table leeft join
df3 = df1.join(df2, lsuffix="_left", rsuffix="_right")
print(df3)

####################################################################

#pandas inner join Dataframes

df3 = df1.join(df2, lsuffix="_left", rsuffix="_right",how = "inner")
print(df3)

#pands left join dataframes
df3 = df1.join(df2, lsuffix="_left", rsuffix="_right", how="left")
print(df3)

#pandas right join dataframes

df3 = df1.join(df2, lsuffix="_left",rsuffix="_right",how = "right")
print(df3)

##########################################################################

#pandas join on columns

df3 = df1.set_index('Courses').join(df2.set_index('Courses'), how = "inner")
print(df3)

#pandas join on columns

df3 = df1.set_index('Courses').join(df2.set_index('Courses'), how = 'left')
print(df3)
    
#pandas join on columns

df3 = df1.set_index('Courses').join(df2.set_index('Courses'), how = 'right')
print(df3)

###########################################################################

#using  pandas.merge()

import pandas as pd
import numpy as np
technologies1={'Courses':['Spark','Pyspark','Python','Pandas'],
               'Fees':[22000,25000,23000,24000],
               'Duration':['30days','40days','55days','40days'],
             }
index_labels1= ['r1','r2','r3','r4']
df1=pd.DataFrame(technologies1,index = index_labels1)
print(df1)

technologies2 = {'Courses': ['Spark','Java','Python','Go'],
                  'Discount':[2000,1300,2300,1200]
                  }
index_labels2 = ['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2, index = index_labels2)
print(df2)

df3 = pd.merge(df1,df2)
df3

df3 = df1.merge(df2)
df3

#####################################################################

#using pandas.concat() to concat two dataFrames

import pandas as pd
df = pd.DataFrame({'Courses':["Spark","Pyspark","Python","pandas"],
                   'Fee':[20000,25000,22000,24000,]})

df1 = pd.DataFrame({'Courses': ["Pandas","Hadoop","Hyperion","Java"],
                    'Fee':[25000,25200,24500,24900]})

df2 = pd.DataFrame({'Duration':['30days','40days','35days','60days','55days'],
                    'Discount':[1000,2300,2500,2000,3000]})
#Using pandas.concat() to concat two dataframes
data = (df, df1)
df2 = pd.concat(data)
df2

#Appending multiple dataframe
df3 = pd.concat([df,df1,df2])
print(df3)

#####################################################################








