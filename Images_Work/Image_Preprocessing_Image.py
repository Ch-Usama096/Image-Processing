#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# Read and Show Image

# In[2]:


# Read The Image
image = cv2.imread(r'C:\Users\Mlogix\Documents\CV Programming\Photos\pokemon_gray.png')

# Show The Image
cv2.imshow('Original Image' , image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Blank And White Image

# In[3]:


# Black Image
black_img = np.zeros([400,400,3] , np.uint8)

# Show The Black Image
cv2.imshow('Black Image' , black_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[4]:


# White Image
white_img = np.ones([400,400,3] , np.uint8)*255

# Show The White Image
cv2.imshow('White Image' , white_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Functions

# In[5]:


# Read The Image
image = cv2.imread(r'C:\Users\Mlogix\Documents\CV Programming\Photos\pokemon_gray.png')

shape = image.shape
type_img = type(image)

print('The Shape of the Image is : {}'.format(shape))
print('The Type of the Image is  : {}'.format(type_img))


# Resize The Image

# In[6]:


# Read The Image
img = cv2.imread(r'C:\Users\Mlogix\Documents\CV Programming\Photos\Pokemon1.jpg')

# Check the Shape of the Image
shape = img.shape
print('The Shape of the Image is : {}'.format(shape))

# Resize The Image
resize_img = cv2.resize(img , (700,500))  
print('After Resize the Image Shape is : {}'.format(resize_img.shape))

# Show The Image
cv2.imshow('Original Image' , resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Write Text and Draw some Shapes

# In[7]:


# Draw Line in the Image

# Read The Image
image = cv2.imread(r'C:\Users\Mlogix\Documents\CV Programming\Photos\pokemon_gray.png')

# Draw Line in the Image
line_img = cv2.line(image , (0,0) , (400,400) , color = (255,0,12) , thickness = 2)

# Show The Image
cv2.imshow('Line Image' , line_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[8]:


# Draw Arrowed Line in the Image

# Read The Image
image = cv2.imread(r'C:\Users\Mlogix\Documents\CV Programming\Photos\pokemon_gray.png')

# Draw Arrowed Line in the Image
arrow_line_img = cv2.arrowedLine(image , (200,200) , (300,300) , color = (255,80,120) , thickness = 2)

# Show The Image
cv2.imshow('Arrowed Line Image' , arrow_line_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


# Draw Rectangle in the Image

# Read The Image
image = cv2.imread(r'C:\Users\Mlogix\Documents\CV Programming\Photos\pokemon_gray.png')

# Draw Rectangle in the Image
rectangle_img = cv2.rectangle(image , (170,50) , (450,463) , color = (255,80,120) , thickness = 2)

# Show The Image
cv2.imshow('Rectangle Image' , rectangle_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[9]:


# Draw Cirlce in the Image

# Read The Image
image = cv2.imread(r'C:\Users\Mlogix\Documents\CV Programming\Photos\pokemon_gray.png')

# Draw Circle in the Image
circle_img = cv2.circle(image , (320,250) , 75 , color = (2,10,5) , thickness = 2)

# Show The Image
cv2.imshow('Circle Image' , circle_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[10]:


# Write Text in the Image

# Read The Image
image = cv2.imread(r'C:\Users\Mlogix\Documents\CV Programming\Photos\pokemon_gray.png')

# Write the Text in the Image
text_img = cv2.putText(image , 'Hello Pokemons!',(10,50) , cv2.FONT_HERSHEY_DUPLEX , 1.5 , color = (25,222,21) , thickness = 3)

# Show The Image
cv2.imshow('Text Image' , text_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# How to Save The Image

# In[12]:


# Read The Image
img = cv2.imread(r'C:\Users\Mlogix\Documents\CV Programming\Photos\Pokemon1.jpg')

# Resize The Image
resize_img = cv2.resize(img , (400,400))

# Convert The GrayScale
gray_img = cv2.cvtColor(resize_img , cv2.COLOR_BGR2GRAY)

# Show The Image
cv2.imshow('Text Image' , gray_img)

if (cv2.waitKey(0) & 0xff == ord('q')):
    
    # Save The Image
    cv2.imwrite('C:\\Users\\Mlogix\\\Documents\\CV Programming\\Photos\\output_img.png' , gray_img)
    
cv2.destroyAllWindows()


# In[ ]:




