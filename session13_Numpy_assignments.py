"""write the program to get the NUmpy version and show the numpy version"""

import numpy as np
print(np.__version__)

##########################################################################

"""write a numpy program to test whether none of the elements of a given 
    array are zero"""
    
import numpy as np

x = np.array([1,2,3,4])
print("Original Array")
print(x)
print("Test if none of the elements of the said array is zero: ")
print(np.all(x))

x = np.array([0,1,2,3,4])
print(x)
print(np.all(x))

############################################################################

"""Write a Numpy program to test if  any of the elements of a given
array are non-zero"""

import numpy as np

x = np.array([1,0,0,0])
print("Original Array")
print(x)
print('Test whether any of the elements of a given array is non-zero: ')
print(np.any(x))

###########################################################################

"""write a Numpy prgram to test a given array element wise for finiteness
    (not infinity or not a number)"""

import numpy as np

a = np.array([1,0,np.nan,np.inf])
print("Original Array")
print(a)
print('Test a given array element-wise for finiteness: ')
print(np.isfinite(a))

#isfinite() function

############################################################################

"""write a Numpy program to test a element-wise for NaN of give array"""

import numpy as np

a = np.array([1,0,np.nan,np.inf])
print("Original Array")
print(a)
print('Test a given array element-wise for finiteness: ')
print(np.isnan(a))

#######################################################################

"""write a Numpy program to create an element-wise comparison
    (greater, greater_equal, less and less_equal of two given arrays"""

import numpy as np

x = np.array([3,5])
y = np.array([2,5])
print("Orginal Arrays")
print(x)
print(y)
print("Comparison - greater")
print(np.greater(x,y))
print("Comparison - greater_equal")
print(np.greater_equal(x,y))
print("Comparison - less")
print(np.less(x,y))
print("Comparison - less_equal")
print(np.less_equal(x,y))

###########################################################################

"""write numpy prgram to create a 3x3 identity matrix"""

import numpy as np
array_2D = np.identity(3)
print('3x3 matrix: ')
print(array_2D)

#########################################################################

"""write a Numpy program to generate a random number between 0 and 1"""

import numpy as np
rand_num = np.random.normal(0,1,1)
print("Random number between 0 and 1: ")
print(rand_num)

##########################################################################

"""write a Numpy program to create a  3x4 array and iterate over it"""

import numpy as np
a = np.arange(10,22).reshape(3,4)
print("Original Array: ")
print(a)
print("Each element of the array is : ")
for x in np.nditer(a):
    print(x,end=" ")
    #print() for vertical


###########################################################################

"""write a numpy program to create a vector of length 5 with values
    evenly distributed between 10 and 50"""

import numpy as np
v = np.linspace(10,49, 5)
#10-start point, 49-end point, 5-nos inn vector
print("Length 10 with values evenly distributed between 10 and 50")
print(v)

###################################################################

"""write a Numpy program to crate a 3x3 matrix with values ranging
    from 2 to 10"""

import numpy as np
x = np.arange(2,11).reshape(3,3)
print(x)

######################################################################

"""write a Numpy program to reverse an array (the first element becomes
    the last"""

import numpy as np
print("Original Array")
x = np.arange(12,38)
print("Original Array")
print(x)
print("Reverse Array: ")
x = x[::-1]
print(x)

#########################################################################

"""write numpy program to compute the multiplication of given two
    matrix"""
    
import numpy as np

p = [[1,0],[0,1]]
q = [[1,2],[3,4]]

print("Original Array")
print(p)
print(q)
result1 = np.dot(p,q)
print("Result of the said matric multiplication: ")
print(result1)

##########################################################################

"""write a numpy program to compute the cross product of two given
    vectors"""

import numpy as np

p = [[1,0],[0,1]]
q = [[1,2],[3,4]]

print("Original Array")
print(p)
print(q)
result1 = np.cross(p,q)
result2 = np.cross(q,p)
print("Cross product of the said two vectors(p,q) ")
print(result1)
print("cross product of the said two vectors(q,p)")
print(result2)

######################################################################

"""write a numpy program to compute the determinant of a given
    square array"""

import numpy as np
from numpy import linalg as LA
a = np.array([[1,0],[1,2]])
print("Original 2-d array")
print(a)
print("Determinant of the said 2-D array: ")
print(np.linalg.det(a))

######################################################################

"""write a Numpy program to compute the eigen values and right eigenvectors
    of a given square array.
"""

import numpy as np
m = np.mat("3 -2;1 0")
print("Original matrix")
print("a\n", m)
w, v = np.linalg.eig(m)
print("Eigenvalues of the said matrix :", w)
print("Eigenvectors of the said matrix: ",v)

############################################################################

"""write a Numpy program to compute the inverse of a given matrix"""

import numpy as np
m = np.array([[1,2],[3,4]])
print("Original Matrix")
print(m)
result = np.linalg.inv(m)
print("Inverse of the said matrix: ")
print(result) 

##############################################################

