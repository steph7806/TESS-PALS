import urllib.request
import csv
import os 
import sys
import pandas as pd
import numpy as np
from os import chdir
from glob import glob
import time 
import smtplib
import requests 
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
#result = pd.concat([a,b], axis=0)
#result.drop_duplicates(keep=False)

#this creates a file 
result.to_csv('result.csv', index=False)

#this implements numpy.all at Arjun's suggestion

#pretend I have code here 

#this condition allows for the email to be sent 

#if (there are no changes)
        # wait 60 seconds,
        time.sleep(60)
        # continue with the script,
        continue
        
    
    else:
        # create an email message with just a subject line,
        msg = 'Subject: TESS Has been Updated with Certain Planets'
       
        fromaddr = 'stephaniegm7806@gmail.com'
        
        toaddrs  = ['steph_7806@berkeley.edu']
                    #Syntax to add more: 'Another_email', 'maybe_another']
        
        # setup the email server,
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # add my account login name and password,
        server.login("******", "*****")
        
        # Print the email's contents
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)
        
        #send the email
        server.sendmail(fromaddr, toaddrs, msg)
        #disconnect from the server
        server.quit()
        
        break
        
        




