"""Write a pandas program to create and display one-dimensional array-like
    containgin an array of data
"""

import pandas as pd
ds=pd.Series([2,4,6,7,8,10])
print(ds)

############################################################################

"""write a pandas program to convert a panda module series to python 
    list and it's type
"""
#asked in intervie
#Pandas series to list

import pandas as pd
ds = pd.Series([2,4,6,8,10])
print('Pandas series and type')
print(ds)
print(type(ds))
print('Convert pandas series to python list')
print(ds.tolist())      
print(type(ds.tolist()))

############################################################################

"""write pandas program to add, substract, multiply and divide
    two series
"""

import pandas as pd

ds1=pd.Series([2,4,6,8,10])
ds2=pd.Series([1,3,5,7,9])
ds = ds1 + ds2
print('Add two series:')
print(ds)
print('substract two series:')
ds = ds1 - ds2
print(ds)
print('Multiply two series:')
ds = ds1 * ds2
print(ds)
print('Divide two Series:')
ds = ds1 / ds2
print(ds)

##########################################################################

""" write a pandas program to compare elements of the series.
    #Samle series: [2,4,6,8,10] [1,3,5,7,9]
"""
ds1 = pd.Series([2,4,6,8,10])
ds2 = pd.Series([1,3,5,7,9])
print('Series1')
print(ds1)
print('Series2')
print(ds2)
print('Comapare the elements of the said series:')
print('Equals')
print(ds1==ds2)
print("greater than:")
print(ds1>ds2)
print("less than:")
print(ds1<ds2)

############################################################

"""write pandas program to to convert a dictionary to a pandas series
    Original Dictionary:
        {'a':100,'b':200,'c':300,'d':400,'e':500}
"""
#dictionary to pandas series

import pandas as pd
d1 = {'a':100,'b':200,'c':300,'d':400,'e':500}
print('Original dictionary:')
print(d1)
new_series = pd.Series(d1)
print('Converted series:')
print(new_series)

##########################################################

""" write pyhton program to covert a NumPy array to a pandas series"""

import numpy as np
import pandas as pd

n_a=np.array([10,20,30,40,50])
print('NumPy array:')
print(n_a)
new_series = pd.Series(n_a)
print('Converted pandas series:')
print(new_series)

#########################################################

""" write pandas program to change the data type of a given
    series
    
    original data series:
    0       100
    1       200
    2    python
    3    300.12
    4       400
    dtype: object
    
    Change the said data type to numeric
    0    100.00
    1    200.00
    2       NaN
    3    300.12
    4    400.00
    dtype: float64
    
"""

import pandas as pd
s1 = pd.Series(['100','200','python','300.12','400'])
print('original data series:')
print(s1)
print('Change the said data type to numeric')
s2 = pd.to_numeric(s1, errors='coerce')
print(s2)

###########################################################################

""" write a pandas program to convert the first column of DataFrame as
    series
"""
#iloc : one of the functions defined in the Pandas module that 
#       helps us to select a specific row or column from the data set.
#iloc[:,0] -> : is rows and after ',' it is columns
# [:,0] for eg :- [2:4,2:3] , 

import  pandas as pd
d = {'col1':[1,2,3,4,7,11],
     'col2':[4,5,6,9,5,0],
     'col3':[7,5,8,12,1,11]
     }
df = pd.DataFrame(d)
print('Original DataFrame')
print(df)
s1 = df.iloc[:,0]
print('\n1st Column as a series')
print(s1)
print(type(s1))

# it is important asked in interview

#####################################################################

# pandas list of series to stack conversion

import pandas as pd
s = pd.Series([['Red','Green','White'],
              ['Red','Yellow'],
              ['Yellow']
                ])
print('Original Series of list:')
print(s)
s = s.apply(pd.Series).stack().reset_index(drop=True)
print('One Series')
print(s)

#.apply() method used to apply various operations
""" DataFrame - stack() function

    The stack() function is used to stack the prescribed level(s)
    from columns to index.
    
    Return a reshaped DataFrame or series
    having a multilevel index with one or more new inner-most 
    levels compared to the current DataFrame
"""
#######################################################################

""" write pandas program to add some data to existing series"""

#.concat()method used to concat the two series

import pandas as pd
s = pd.Series(['100','200','Python','300.12','400'])
print(s)
print('\n Data Series after some data:')
new_s = pd.concat([s, pd.Series([500, "php"])], ignore_index = True)
print(new_s)

######################################################################

"""write a pandas program to change the order of Index of a given
    series
    
    Orginal Data Series:
    A    1
    B    2
    C    3
    D    4
    E    5
    dtype: int64
    
    B    2
    D    4
    A    1
    C    3
    E    5
    dtype: int64
    
"""
#.reindex() used to change the order of the index

import pandas as pd
s = pd.Series(data = [1,2,3,4,5], index = ['A','B','C','D','E'])
print('Orginal Data Series:')
print(s)
s = s.reindex(index = ['B','D','A','C','E'])
print(s)

##############################################


















