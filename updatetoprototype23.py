#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import urllib.request
import csv
import os 
import sys
import pandas as pd

#this makes sure that I'm in the right directory
os.chdir('/Users/stephaniegomez/Documents/EXOFOPCSV/')

#this downloads the csv file from EXOFOP 
print('Downloading EXOFOP Table CSV as "comparison.csv"...')
url = 'https://exofop.ipac.caltech.edu/tess/download_toi.php?sort=toi&output=csv'
urllib.request.urlretrieve(url, '/Users/stephaniegomez/Documents/EXOFOPCSV/comparison.csv')

#this reads the csv files and compares for duplicates 
a = pd.read_csv('mainlist.csv')
b = pd.read_csv('comparison.csv')

#this merges the files to check for duplicates
result = pd.concat([a,b], axis=0)
result.drop_duplicates(keep=False)

#this creates a file 
result.to_csv('result.csv', index=False)

#this checks if the file is empty, thus signaling if there has been an update
if os.path.getsize('/Users/stephaniegomez/Documents/EXOFOPCSV/result.csv') > 0:
    print("There has been an update!")
    os.remove("mainlist.csv")
    os.rename(r'/Users/stephaniegomez/Documents/EXOFOPCSV/comparison.csv',r'/Users/stephaniegomez/Documents/EXOFOPCSV/mainlist.csv')
else:
        print("There are no updates.")
        os.remove('comparison.csv')
        os.remove('result.csv')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




