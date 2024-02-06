""" write a pandas program to create a dataframe from a dictionary
and display it 
Sample Data: {'X':['1,2,3,4,5],
              'Y:[6,7,8,9,10']
              'Z:[11,12,13,14,15]}
"""
import pandas as pd
import numpy as np

data ={'X':[1,2,3,4,5],
      'Y':[6,7,8,9,10],
      'Z':[11,12,13,14,15]}
df = pd.DataFrame(data)
print(df)


#####################################################################

""" Display python dictionary data and list lables"""


exam_data = {'name': ['Dinesh','Ganesh','Rajesh','Vijay','Chaitanya','dhanush'],
            'score': [17,16,20,np.nan,14,18],
            'attempts':[1,2,1,3,3,1],
            'qualify':['yes','yes','no','no','yes','yes'],
            }
labels =['a','b','c','d','e','f']
df = pd.DataFrame(exam_data, index= labels)
print(df)

####################################################################

"""write pandas program to display a summary of the basic information
about the dataframe"""

exam_data = {'name': ['Dinesh','Ganesh','Rajesh','Vijay','Chaitanya','dhanush'],
            'score': [17,16,20,np.nan,14,18],
            'attempts':[1,2,1,3,3,1],
            'qualify':['yes','yes','no','no','yes','yes'],
            }
labels =['a','b','c','d','e','f']
df = pd.DataFrame(exam_data, index= labels)
print(df)

df.describe()   #to display summary
df.info() # to display summary

################################################################

"""write pandas program to get first three rows of given dataframe"""

df=pd.DataFrame(exam_data)
print(df)
print("First three rows of the data frame: ")
df.iloc[0:3]
#also
df.iloc[:3]

#########################################################################

""" write python program to select name and score column from given
    dataframe"""

print("select specific columns: ")
print(df[['name','score']])

#########################################################################

""" write python program to select specified columns and rows
    from the dataframe"""

df.loc[:,['score','qualify']]

# to call specific columns


###########################################################################
"""write python program to select no of rows where the numnber of
attempts in the examination is greater than 2"""


print('Number of attempts in the exam is greateh than 2: ')

print(df[df['attempts']>2])
#also
df.query('attempts > 2')
#
df2 = df.loc[df.attempts>2]
df2


###########################################################################

""" write python program to count the number of rows and columns of 
    Dataframe """

print('Number of rows in given dataframe: ')
rows_count = len(df.index)
print(rows_count)

print('Number of columns in given dataframe: ')
col_count = len(df.axes[1])
print(col_count)

#sir's method

total_rows = len(df.axes[0])
total_cols = len(df.axes[1])
print('number of rows: ' +str(total_rows))
print('number of columns: '+str(total_cols))

##########################################################################

"""write pandas program to selec the rows where the score is missing
"""
    
print('Rows where the score is missing: ')
print(df[df['score'].isnull()])

###########################################################################

"""write pandas program to select rows betwn 15 and 20 (inclusive)"""

print('Rows where score between 15 and 20 (inclusive): ')
print(df[df['score'].between(15,20)])


#########################################################################

""" write pandas program to select the rows where the number of attempts
 in the exam is less than 2 and score greater than 15"""

import pandas as pd
import numpy as np
exam_data = {'name': ['Dinesh','Ganesh','Rajesh','Vijay','Chaitanya','dhanush'],
            'score': [17,16,20,np.nan,14,18],
            'attempts':[1,2,1,3,3,1],
            'qualify':['yes','yes','no','no','yes','yes'],
            }
labels =['a','b','c','d','e','f']
df = pd.DataFrame(exam_data, index= labels)
print(df)

print(df[(df['attempts']<2) & (df['score']>15)])


############################################################################

"""write pandas program to change the score in row 'd' to 11.5 """

print('Change the score in row d to 11.5 : ')
df.loc['d','score'] = 11.5
print(df)

########################################################################

"""write pandas program to calculate the sum of the examination 
    attempts by the students"""

print("\n Sum of the examination attempts by the students: ")
print(df['attempts'].sum())

########################################################################

""" write a search pandas program to calcualte the mean of all
    students score"""

print(df['score'].mean())


############################################################################

""" write pandas program to append a new row 'k' to dataframe with given
    values for each column 
"""

df.loc['g'] = ['surya','23','2','yes']
print(df)

############################################################################

"""write pandas program to sort the dataframe first by 'name' in 
    descending order then by 'score' in ascending order
"""
import pandas as pd
import numpy as np
exam_data = {'name': ['Dinesh','Ganesh','Rajesh','Vijay','Chaitanya','dhanush'],
            'score': [17,16,20,26,14,18],
            'attempts':[1,2,1,3,3,1],
            'qualify':['yes','yes','no','no','yes','yes'],
            }
labels =['a','b','c','d','e','f']
df = pd.DataFrame(exam_data, index= labels)
print(df)

df.sort_values(by=['name'], ascending=[False])
print(df)

df.sort_values(by=['score'], ascending=[True])
df

##########################################################################

"""write pandas program to replace the 'qualify' column values 
    yes and no with true and false
"""

df['qualify'] = df['qualify'].map({'yes':True, 'no':False})
print(df)

#imp, project dev


##########################################################################

"""write a pandas program to change the name 'Rajesh' to 'Rohit' in name
    column of the dataframe
"""

df['name'] = df['name'].replace('Rajesh','Rohit')
print(df)
# Rajesh -> old name
# Rohit -> New name

##########################################################################


""" write a pandas program to insert a new column in existing dataframe """

color = ['Red','orange','Blue','White','Yellow','black']
df2 = df.assign(Colurs=color)
print(df2)

############################################################################

"""write a pandas program to iterate over rows in dataframe"""
import pandas as pd
import numpy as np
exam_data = {'name': ['Dinesh','Ganesh','Rajesh','Vijay','Chaitanya','dhanush'],
            'score': [17,16,20,26,14,18],
            'attempts':[1,2,1,3,3,1],
            'qualify':['yes','yes','no','no','yes','yes'],
            }
labels =['a','b','c','d','e','f']
df = pd.DataFrame(exam_data, index= labels)
print(df)
for index,row in df.iterrows():
    print(row['name'],row['score'])

############################################################################

"""write a search pandas program to get a list from dataframe column headers"""




















