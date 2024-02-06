
import pandas as pd
df = pd.read_csv('seeds_data.csv')
df

################################################################

#query operation

df.query('Area == 15.26')
print(df)

df.query('Area != 15.26')

#column position

row_column = df.shape[0]
col_column = df.shape[1]
print(row_column)
print(col_column)

#Summary of the dataset
df.info()

#first three rows
df.iloc[:3]

#to select specific columns
print(df[['Area','Compactness']])

#to select specified columns and rows

df.loc[:,['Area','Width']]

#Assymetry_coeff > 2
df[df['Assymetry_coeff']>2]
#also
df.query('Assymetry_coeff > 2')
df[df['Type']>2]

#where width is null
df[df['Width'].isnull()]
#nothing is null

#Area betn 15 and 20
df[df['Area'].between(15,20)]


#type<2 and area>15

df2 = df[(df['Type']<2) & (df['Area']>15)]
df2

# area of index 2 to 14

df.loc[2,'Area'] = 14
print(df)

# sum of Width
print(df['Width'].sum())

#mean of Type Column
print(df['length'].mean())

#adding row to dataframe
df.loc[210] = [10.2,15.2,0.333,4.232,3.33,1.222,4.42,4]

#sorting area in descending order
df.sort_values(by=['Type'], ascending=[False])
df

#iterating
for index,row in df.iterrows():
    print(row['Area'], row['Type'])

df.to_string()
