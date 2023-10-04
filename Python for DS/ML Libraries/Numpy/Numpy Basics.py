#!/usr/bin/env python
# coding: utf-8

# # Numpy Basics

# In[13]:


##Why it is useful: Memory-efficient container that provides fast numerical operations.

import numpy as np
a = np.zeros(3)
a


# In[4]:


z = np.zeros(10)
z


# In[9]:


y = np.ones(12)
y
type(y[1])


# In[14]:


x = np.linspace(2,10,6) #From 2 to 10 , with 5 elements.
x


# ## Creating Arrays
# ### Manual Construction of Arrays

# In[15]:


#1-D Array
a = np.array([0,1,2,3])
a


# In[16]:


a.ndim


# In[20]:


a.shape


# In[21]:


len(a)


# In[26]:


#2-D , 3-D Array
b = np.array([[0,1,2] , [3,4,5]]) # 2 X 3 array
b


# In[27]:


e = np.array([[2,4,6] , [4,8,9] , [1,7,6]]) #3 X 3 array
e


# In[29]:


e.shape


# Exercise: Simple arrays
# 
#     Create a simple two dimensional array. First, redo the examples from above. And then create your own: how about odd numbers counting backwards on the first row, and even numbers on the second?

# In[30]:


ev_od = np.array([[9,6,3] , [2,4,6]])
ev_od


# In[31]:


len(ev_od)


# In[33]:


np.shape([[9,6,3] , [2,4,6]])


# In[34]:


ev_od.ndim


# # Basic data types
# in some instances, array elements are displayed with a trailing dot (e.g. 2. vs 2). This is due to a difference in the data-type used:

# In[35]:


a = np.array([1,2,3])
a.dtype


# In[36]:


b = np.array([3.,4.,5.])
b.dtype


# In[37]:


c = np.array([3,4,5] ,dtype = float)#We can aslo specify the type of data , but the default is Float type
c.dtype
#there are also other Data types like Complex , Bool , Strings , int32 , int 64 etc etc


# # Basic visualization

# In[39]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[40]:


import matplotlib.pyplot as plt


# In[45]:


print("1D Plotting")
x = np.linspace(0, 3, 20)

y = np.linspace(0, 9, 20)
plt.plot(x, y)


# In[44]:


plt.plot(x, y , 'o')
#plt.show not needed with interactive plots!


# # #
# 
# Exercise: Simple visualizations
# 
#     Plot some simple arrays: a cosine as a function of time and a 2D matrix.
# 
#     Try using the gray colormap on the 2D matrix.
# 
# 

# In[49]:


#2D arrays (such as images):
rng = np.random.default_rng(27446968)#This line initializes a random number generator with a specific seed value (27446968). Using a fixed seed ensures that the random numbers generated are reproducible, meaning that if you run the code with the same seed, you'll get the same random numbers every time.
image = rng.random((30, 30))#Here, you use the random number generator (rng) to create a 30x30 2D array filled with random numbers between 0 and 1. This array represents your "image," although it's just a grid of random values.
plt.imshow(image, cmap=plt.cm.hot)#plt.imshow(image, cmap=plt.cm.hot): This line uses Matplotlib to display the 2D array (image) as an image. The cmap=plt.cm.hot argument specifies the colormap to be used for mapping the values in the array to colors. In this case, you're using the "hot" colormap, which represents lower values with cooler colors (e.g., blue) and higher values with warmer colors (e.g., red).
plt.colorbar()#This line adds a colorbar to the plot. The colorbar is a side scale that shows the mapping of values to colors in the image. It helps interpret the colors in the image and their corresponding values in the array.


# In[50]:


import numpy as np
import matplotlib.pyplot as plt

# Create a 2D matrix
matrix = np.random.rand(10, 10)  # Generate a 10x10 matrix of random numbers

# Plot the 2D matrix as an image
plt.figure(figsize=(6, 6))
plt.imshow(matrix, cmap=plt.cm.hot, interpolation='nearest')
plt.colorbar()
plt.title('2D Matrix')
plt.show()


# In[51]:


import numpy as np
import matplotlib.pyplot as plt

# Create a 2D matrix
matrix = np.random.rand(10, 10)  # Generate a 10x10 matrix of random numbers

# Plot the 2D matrix as an image in grayscale
plt.figure(figsize=(6, 6))
plt.imshow(matrix, cmap='gray', interpolation='nearest')
plt.colorbar()
plt.title('2D Matrix (Grayscale)')
plt.show()


# 

# In[52]:





# In[54]:





# In[ ]:




