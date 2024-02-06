#---------------------Crime_data.csv----------------------------#

import pandas as pd
import numpy as np

df = pd.read_csv("crime_data.csv")
df

df = pd.DataFrame(df)
print(df.dtypes)

df1 = df.convert_dtypes()
print(df1.dtypes)

# change all columns to same type
df = df.astype(str)
print(df.dtypes)

df.describe()

df.size
#250
df.dtypes
#dtype: object
df.columns
df.columns.values
#Index(['Unnamed: 0', 'Murder', 'Assault', 'UrbanPop', 'Rape'], 
#       dtype='object')
df.index
#RangeIndex(start=0, stop=50, step=1)
df.shape
#(50, 5)

df = pd.DataFrame(df)
df2 = df.rename({'Unnamed: 0':'Country'}, axis=1)
df2

df2['Country']
#accessing the one column

df2[['Country','Rape']]
#acessing two columns
df2['Country'][10]

#converting dtypes of dataframe
df2 =df2.astype({'Murder':int,'Assault':float},errors='ignore')
df2

cols=['Murder','Assault']
df2[cols]=df[cols].astype('int',errors='ignore')
df2
df2.dtypes

#Substracting from column assault
df2['Assault'] = df2['Assault'] - 10
df2["Assault"]

#name changed of column
df3 = df2.rename({'UrbanPop':'Urban'},axis=1)
df3

#df3 is assign to n now it is main
n = pd.DataFrame(df3)
n

#Drop rows and columns by labels

#here labels are not giving to index

# so, drop rows and columns by index

d = n.drop(n.index[1])
d #index 1 is removed

d = n.drop(d.index[[2,3]])
d #index 2 is removed multi index


d = n.drop(0)
d

d = n.drop([10,12])
d

d = n.drop(range(20,30))
d
#excluding 30

#dropping columns
m = n.drop(['Rape'],axis=1)
m
#dropped by label
m = n.drop(columns=['Urban'],axis=1)
m
#dropped by labels
m = n.drop(n.columns[1],axis = 1)
m
#dropped by index

df.drop(df.columns[2],axis=1,inplace=True)
df

#dropping by columns
m = n.drop(['Country','Assault'],axis=1)
m

#dropping by columns index
m = n.drop(n.columns[[0,1]],axis=1)
m

#dropping by list of columns
lisCol=['Country','Murder','Assault']
m = n.drop(lisCol,axis=1)
m.columns

df = pd.DataFrame(df)
df

#slicing specific rows using iloc
m = df.iloc[:,0:2]
m

m = d.iloc[0:2,:]
m

m = d.iloc[1:2,1:3]
m

m = d.iloc[[1,2,3]]
m

m = d.iloc[-3:]
m

m = d.iloc[3:]
m

m = d.iloc[1:5]
m
#excluding 5th row

#slicing specific columns using loc
m = d.loc[:,['Murder','Assault','Rape']]
m

m = d.loc[:,'Rape']
m

#---------------------------bank_data-----------------------------#

import pandas as pd
import numpy as np

df = pd.read_csv("bank_data.csv")
df

df.columns
df.size
df.index
df.shape
df.dtypes

df[['age','balance','housing']]

df['age'][1000]

df1 = df.convert_dtypes()
print(df1.dtypes)

df.dtypes

df = df.astype(str)
print(df.dtypes)

df.describe

lisCol= ['poutunknown', 'con_cellular', 'con_telephone', 'con_unknown',
'divorced', 'married', 'single', 'joadmin.', 'joblue.collar',
'joentrepreneur', ]
df2 = df.drop(lisCol, axis=1)
df2

df2.index

df2.columns

r = df2.drop(['johousemaid', 'jomanagement', 'joretired', 'joself.employed',
'joservices', 'jostudent', 'jotechnician', 'jounemployed', 'jounknown',
'y'],axis=1)
r

w = r.drop(range(10000,40000))
w

w.size

s = w.drop(w.index[[]])
s

s = w.iloc[:,0:2]
s

s = w.iloc[1:2,1:3]
s

s = w.iloc[-3:]
s

s = w.loc[:,['age','balance']]
s

s = w.loc[:,'housing']
s


#---------------------------loan_csv-------------------------#

import pandas as pd
import numpy as np

df = pd.read_csv("loan.csv")
print(df)

df.index
df.size
df.columns
df.shape

df[['id', 'member_id', 'loan_amnt']]

df['loan_amnt'][29]


df1 = df.convert_dtypes()
print(df1.dtypes)

df.dtypes

df = df.astype(str)
print(df.dtypes)

df.describe

lisCol= ['num_tl_90g_dpd_24m', 'num_tl_op_past_12m', 'pct_tl_nvr_dlq',
'percent_bc_gt_75', 'pub_rec_bankruptcies', 'tax_liens',
'tot_hi_cred_lim', 'total_bal_ex_mort', 'total_bc_limit',
'total_il_high_credit_limit' ]
df2 = df.drop(lisCol, axis=1)
df2

df2.index

df2.columns

k = df2.drop(df2.index[100:1000])
k

k.size

p = k.iloc[:,0:2]
p

p = k.iloc[1:5,1:34]
p

p=k.iloc[-3:]
p

p = k.iloc[30:]
p

p = k.loc[:,['member_id','loan_amnt']]
p

p = k.loc[:,'purpose']
p

p.size

