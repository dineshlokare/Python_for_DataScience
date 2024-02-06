
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.show()

#this is called line chart

#############################################################################

#Multiline plots
import matplotlib.pyplot as plt
x = range(1,5)
plt.plot(x,[xi*1.5 for xi in x])

plt.plot(x,[xi*3.0 for xi in x])

plt.plot(x,[xi/3.0 for xi in x])

plt.show()

##################################################################

#Grid, Axes and labels
#Adding a grid

import matplotlib.pyplot as plt 
import numpy as np
x = np.arange(1,5)
plt.plot(x, x*1.5, x, x*3.0, x, x/3.0)
plt.grid(True)
plt.show()

################################################################

#Handling Axes

import matplotlib.pyplot as plt 
import numpy as np
x = np.arange(1,5)
plt.plot(x, x*1.5, x, x*3.0, x, x/3.0)
plt.axis() #shows the current axis limits values
plt.axis([0,5,-1,13])
# [xmin,xmax,ymin,ymax]
plt.show()

###################################################################3

#Adding labels

import matplotlib.pyplot as plt
plt.plot([1,3,2,4])

plt.xlabel("This is the x axis")

plt.ylabel("This is the Y axis")

plt.show()

#####################################################################

#Adding a title

import matplotlib.pyplot as plt
plt.plot([1,3,2,4])

plt.title('Simple Plot')
plt.show()

#Matplotlib provides a simple function, plt.title() to add a title

#########################################################################

#Adding a legend

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,5)
plt.plot(x, x*1.5, label = 'Normal')
plt.plot(x, x/3.0, label = 'slow')
plt.legend()
plt.show()

##################################################################

""" Colour abbreviation

color   Name

 b      blue
 c      cyan
 g      green
 k      black
 m      magenta
 r      red
 w      white
 y      yellow
"""
#Control colors

import matplotlib.pyplot as plt
import numpy as np
y = np.arange(1,5)
plt.plot(y,'y')
plt.plot(y+1, 'm')
plt.plot(y+2, 'c')
plt.show()

###############################################################

#specifying styles in multiline plots

import matplotlib.pyplot as plt
import numpy as np
y = np.arange(1,3)
plt.plot(y, '--',y+1,'-.',y+2,':')
plt.show()

#########################################################################

"""Style abbrevation
    - solid line
    -- dashed line
    -. dash-dot line
    
"""
#####################################################

#Markers control

import matplotlib.pyplot as plt 
import numpy as np
y = np.arange(1,3,0.2)
plt.plot(y, 'x',y+0.5, 'o',y+1, 'D',y+1.5, '^',y+2, 's')
plt.show()

######################################################################
#Histogram charts

import matplotlib.pyplot as plt
import numpy as np
y = np.random.randn(1000)
plt.hist(y);
plt.show()

#########################################################################

import matplotlib.pyplot as plt
plt.bar([1,2,3],[3,2,5])
plt.show()

#Used in EDA -> Exploratory Data Analysis

""" b
The bar() fucntion is used to generate bar charts in Matplotli"""

##########################################################################

#Scatter Plots

#Bivariate analysis
#Scatter plots display values for the two sets of data
#The data visualizationis done
#as collection of points not connect by lines.
#Each of them has its coordinates
#determined by the value of the variables
#(one variable determines the X position),
#The other the Y position

import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.scatter(x,y)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()

size = 50*np.random.randn(1000)
colors = np.random.rand(1000)
plt.scatter(x,y,s=size,c=colors);
plt.show()

####################################################################

#Adding text
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-4, 4, 1024)
y = .25 * (x + 4.) * (x+1.) * (x-2.)
plt.text(-0.5, -0.25, 'Brackmard minimum')
plt.plot(x, y, c='k')
plt.show()

####################################################################

#How to use Seaborn for Data Visualization
#pip install seaborn

import seaborn as sns
import pandas
import matplotlib.pyplot as plt
#Seaborn has 18 in-built datasets,
#that can be found using the following command,
sns.get_dataset_names()
df = sns.load_dataset('titanic')
df.head()

#Count Plot

"""A count plot is helpful when dealing with categoricl values. It is used
to plot the frequency of the different categories.
The column sex contains categorical data in the titanic
data, i.e., male and female"""

sns.countplot(x='sex',data=df)
#x- The name of the column
#data- The dataframe
sns.countplot(x='sex', hue='survived',data=df, palette ='Set1')
sns.countplot(x='sex',hue='survived', data=df, palette='Set2')
sns.countplot(x='sex',hue='survived', data=df, palette='Set3')

#hue - The name of the categorical column to split the bars.

#palette - the color palette to be used.

####################################################################

#KDE plot
#A Kernel Density Estimate (KDE) plot is used
#to plot the distribution of continuous data.
sns.kdeplot(x='age',data = df, color = 'black')



#x - The name of the column,
#data - The dataframe
#color - The color of the graph. YOu can find a list of columns
################################################################
#Distribution plot
sns.displot(x='age',kde=True,bins=6,data=df)


#kdf- It is set to False by default. However, if you wish

#bins - The number of bins/bars
#The lower the number, wider the bars ans wider the interval 

sns.displot(x='age',kde=True,bins=5, hue=df['survived'],palette = 'Set1',
            data=df)

#Scatter plot
#for this plot and the plots below,
#we will be working with the iris dataset.
#The iris dataset contains data related
#The flower's petal size(petal length and petal width)
#and sepal size (sepal length and sepal width)
#These features are used to classify the type of iris


df = sns.load_dataset('iris')
df.head()
#Scatter plots help understand co-relation between data,
sns.scatterplot(x='sepal_length',y='petal_length',data=df,hue='species')

#################################################################

#Joint plot

#A joint plot is also used to plot the correlation between
sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='reg')

sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='hist')

sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='kde')

""" kind - The kind of plot to be plotted
    It can be one of the following
    
    'Scatter', 'hist,'hex','kde','reg','resid'

"""

#####################################################################

#Pair plots

sns.pairplot(df)

########################################################################

#A heat map can be used to visualize confusion, matrices, and correlaion.

corr = df.corr()
sns.heatmap(corr)

#######################################################################

