#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os


# # OS Library

# ## OS Environment and Machine Information

# Number of CPUs
# 
# Linux: `nproc`

# In[ ]:


os.cpu_count()


# A mapping of environment variables
# 
# Linux: `printenv`

# In[ ]:


os.environ


# We can pull strings from the mapping directly with keys
# 
# Linux: `printenv HOME`

# In[ ]:


os.environ['home']


# A method for selecting specific variables

# In[ ]:


os.getenv('Home')


# Environment values can be manipulated with string methods

# In[ ]:


os.getenv('Home') + '\Documents'


# WHO AM I: find the current user
# 
# Linux: `whoami`

# In[ ]:


os.getlogin()


# We can find the process id for a script or program.
# In this case it's running within the jupyter notebooks kernel and that process is fixed.
# 
# If we had a script to check the process id and ran it multiple times it would change each time.

# In[ ]:


os.getpid()


# ## Directory Management

# ### Current Working Directory

# Get current working directory
# 
# Linux: `pwd`

# In[ ]:


os.getcwd()


# ### Listing Directory Contents

# Python command to list files and directories in current directory
# 
# Functions like `ls -a` in linux systems

# In[ ]:


os.listdir()


# Navigate to parent directory
# 
# Linux: `ls -a ..`

# In[ ]:


os.listdir("..")


# Navigate to my C: directory
# 
# Linux: `ls -a C:/`

# In[ ]:


os.listdir('C:/')


# ### Navigating to Different Directories

# Change working directory to parent directory
# 
# Linux: `cd ..`

# In[ ]:


os.chdir("..")
os.getcwd()


# Navigate locally to OSDemo Directory
# 
# Linux: `cd OSDemo`

# In[ ]:


os.chdir("OSDemo")
os.getcwd()


# Navigate to home directory
# 
# Linux: cd ~

# In[ ]:


os.chdir(os.getenv('HOME'))
os.getcwd()


# In[ ]:


os.chdir("Documents/Revature/OSDemo")


# ### Creating Directories

# Creating a new directory locally in our current working directory
# 
# Linux: `mkdir testdir`

# In[ ]:


os.mkdir('testdir')
os.listdir()


# Creating a new directory using full path
# 
# Linux: `mkdir C:/testdir`

# In[ ]:


os.mkdir('C:/testdir')
os.listdir('C:/')


# ### Removing Directories

# Remove directory locally
# 
# Linux: `rmdir testdir`

# In[ ]:


os.rmdir('testdir')
os.listdir()


# Remove directories absolutely
# 
# Linux: `rmdir C:/testdir`

# In[ ]:


os.rmdir('C:/testdir')
os.listdir('C:/')


# ### Recursive Directory Management

# Create nested directories with intermediate directories
# 
# Linux: `mkdir -p listdir1/listdir2`

# In[ ]:


os.makedirs('listdir1/listdir2')
os.listdir()


# In[ ]:


os.listdir('listdir1')


# Remove nested directories along with parent directories
# 
# Linux: `rmdir -p listdir1/listdir2`

# In[ ]:


os.removedirs('listdir1/listdir2')
os.listdir()


# ## File Management

# In[ ]:


os.listdir()


# Create a file in our current working directory
# 
# Also creates a file descriptor which we can access the file with
# 
# Linux: `touch test.py`

# In[ ]:


newFile = os.open('test.py', os.O_CREAT)
os.listdir()


# File descriptor

# In[ ]:


newFile


# We can try to write to the file, but we don't have permission to do so and we get an OSError

# In[ ]:


os.write(newFile, b'b')


# Close the file descriptor

# In[ ]:


os.close(newFile)


# Open the file with read and write privileges

# In[ ]:


accessedFile = os.open('test.py', os.O_RDWR)


# Read bytes from the file

# In[ ]:


os.read(accessedFile, 10)


# Set position of file descriptor to beginning

# In[ ]:


os.lseek(accessedFile, 0, 0)


# Write bytes to file based on position

# In[ ]:


os.write(accessedFile, b'bad')


# Close file descriptor

# In[ ]:


os.close(accessedFile)


# Remove a file
# 
# Linux: `rm test.py`

# In[ ]:


os.remove('test.py')
os.listdir()

