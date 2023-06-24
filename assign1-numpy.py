#Create a null vector of size 10 but the fifth value which is 1.

import numpy as np
null_vector= np.zeros(10)
null_vector[4]=1
print(null_vector)


#2. Create a vector with values ranging from 10 to 49.
import numpy as np
vector = np.arange(10,50)
print(vector)

#3. Create a 3x3 matrix with values ranging from 0 to 8.
import numpy as np
matrix =np.arange(0,9).reshape(3,3)
print(matrix)


#4. Find indices of non-zero elements from [1,2,0,0,4,0]
import numpy as np
l = [1,2,0,0,4,0]
arr = np.array(l)
l_new=list(np.nonzero(arr[0]))
print(l_new)


#5. Create a 10x10 array with random values and find the minimum and maximum values.
import numpy as np
x = np.random.randint(100,size=(10,10))
print("original array:")
print(x)
xmin,xmax = x.min(),x.max()
print("minimum and maximum values of the original array:")
print(xmin,xmax)

#6. Create a random vector of size 30 and find the mean value.
import numpy as np
v = np.random.random(30)
mean_value = v.mean()
print(mean_value)