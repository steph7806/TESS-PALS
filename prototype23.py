#!/usr/bin/env python
# coding: utf-8

# In[1]:


#this downloads the csv file from exofop
import urllib.request
import csv
import os 

print('Beginning file download with urllib2...')

url = 'https://exofop.ipac.caltech.edu/tess/download_toi.php?sort=toi&output=csv'
urllib.request.urlretrieve(url, '/Users/stephaniegomez/Downloads/comparison.csv')

#this compares the values of the dowloaded table along with a "master"file
#if it finds a change, it replaces the old masterfile with the most recent itteration
input_file1 = "/Users/stephaniegomez/Downloads/masterlist.csv"
input_file2 = "/Users/stephaniegomez/Downloads/comparison.csv"
            
            
with open('masterlist.csv', 'r') as t1, open('comparison.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('update.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)
            print("There has been an update!")
            os.remove("masterlist.csv")
            os.rename(r'/Users/stephaniegomez/Downloads/comparison.csv',r'/Users/stephaniegomez/Downloads/masterlist.csv')
        else:
            print("No Updates")
            os.remove("comparison.csv")


# In[ ]:





# In[ ]:





# In[ ]:




