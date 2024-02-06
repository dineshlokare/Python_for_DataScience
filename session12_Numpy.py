#What is Numpy?

"""The numpy library is a popular open-source python
    library used for scientific computing applications,
    and it stands for Numerical pyython
    which is consisting of multidimensional array
    objects and a collection of routines for processing those arrays."""

"""Install python numpy library
    goto base terminal and on prompt
    pitp install numpy
    Install Numpy Library 
    conda install numpy"""
    
"""While a python list can contain different data types within
    a single list, all of the elements in a NUmpy array should be
    homogenous"""
    
#Arrays in Numpy
#create an array

import numpy as np 
arr = np.array([10,20,30])
print(arr)

#creatae multi dimensionl array

arr = np.array([[10,20,30],[40,50,60]])
print(arr)

#Represent the minimum dimensions
#Use ndmin param to specify how many minimum
#dimensions you wnated to create an array width 
# Minimum dimension

arr = np.array([10,20,30],ndmin = 2)
print(arr)

arr = np.array([10,20,30,40],ndmin=3)
print(arr)

#change the data type
#dtype parameter

arr = np.array([10,20,30],dtype = complex)
print(arr)

#Get the Dimension of array

arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr.ndim)
print(arr)

##############################################################

#Finding the size of each item in the array

arr = np.array([10,20,30])
print("Each item contain in bytes: ",arr.itemsize)

#Finding the datatype of each array item

arr = np.array([10,20,30])
print("Each item is of the type: ", arr.dtype)

################################################################

#Get the shape and size of Array

arr = np.array([[10,20,30],[40,50,60]])
print("Array Size: ",arr.size)
print("Array Shape: ",arr.shape)

###################################################################

#Creating array from list with type float

arr = np.arange(0,20,3)
print("A sequential array with steps of 3: \n",arr)
#A sequential array with step of 3


#Access single element using index

arr = np.arange(11)
print(arr)
# output : [ 0  1  2  3  4  5  6  7  8  9 10]

print(arr[2]) #-> 2

print(arr[-2]) #-> 9

#####################################################################

#Multi Dimensional Array Indexing
# Access multi-dimensional array element
# Using array indexing

arr = np.array([[10,20,30,40],[50,60,70,80]])
print(arr)

print(arr.shape)

#rows start from 0 and column from 0
print(arr[1,1])
#60
print(arr[0,3])
#40

print(arr[1,-1])
#80

########################################################################

#Access array elements using slicing

arr = np.array([0,1,2,3,4,5,6,7,8,9])
x=arr[1:8:2]  #start:end in step of 2
print(x)

x=arr[-2:10]
print(x)
#from last -2 -> 8no and 10-> 9no

######################################################################

#indexing in numpy

multi_arr = np.array([[10,20,10,40],
                [40,50,70,90],
                [60,10,70,80],
                [30,90,40,30]])
multi_arr
#slicing array

multi_arr[1,2] #- To access the value at row 1 and column 2

multi_arr[1,:] #- To get the value at row 1 and all column

multi_arr[:,1] #- Access the value at all rows and columns 1

x = multi_arr[:3,::2] #columns from 0 to 3, in all selected rows and columns
print(x)

#######################################################################

#Integer array indexing

#Integer Array indexing alows the selection of arbitrary items:
    
#Integer array indexing

arr = np.arange(35).reshape(5,7)
print(arr)

#####################################################################

#Boolean Indexing

#This advanced indexing of Boolean types,
#such as may be returned from comparison operators
#Use this method when we want to pick elements
#from the array which satisfy some conditons

arr = np.arange(12).reshape(3,4)
print(arr)

rows = np.array([False, True, True])

wanted_rows = arr[rows,:] #not 0th row only first and second
print(wanted_rows) #In selected rows all rows and columns

##########################################################################

#Convert Numpy array to python list

#Convert one dimensional array to list

#create array
array = np.array([10,20,30,40])
print("Array: ",array)
print(type(array))

#converting list
lst = array.tolist()
print("list: ",lst)
print(type(lst))


#Convert Multi Dimensional array to list

array = np.array([[10,20,30,40],
                  [50,60,70,80],
                  [60,30,20,10]])
print("Array",array)

lst = array.tolist()
print("List: ",lst)

########################################################################

#Convert Python List to Numpy array

#Create list
lst = [20,30,50,70]

#convert array
array = np.array(lst)
print("Array: ",array)

#Two methods:
#numpy.array()
#numpy.asarray()

#Use array
list = [20,40,50,60]
array = np.asarray(list)
print("array: ",array)
print(type(array))

#####################################################
#Numpy Properties

#Resize your array

#ndarray.shape

# to get shape of python NUmpy array 

#shape
array = np.array([[10,20,30,40],[50,60,70,80]])
array.shape=(4,2)
print(array)

arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape)

######################################################################

#Operations using in NUmpy

#Numpy's operations are divided into three main
#categories:
    
        """Fourier Transform and shape Manipulation
            Mathematical and logical Operations
            Linear Algebra and Random Number Generation"""

#Arithmetic operations

#Arithmetic operators on arrays apply elementwise. A new array is

#Apply arithmetic operations on numpy arrays

arr1 = np.arange(16).reshape(4,4)
arr2 = np.array([1,2,3,4])

