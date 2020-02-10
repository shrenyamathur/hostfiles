#!/usr/bin/env python
# coding: utf-8

# In[1]:
import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug import secure_filename
from azure.storage.blob import *
import string, random, requests
import configparser
import mysql.connector
import pymysql


app = Flask(__name__, instance_relative_config=True)

Config = configparser.ConfigParser()
Config.read("config2.py")

# Account name
account = Config.get('DEFAULT', 'account')
# Azure Storage account access key 
key = Config.get('DEFAULT', 'key')
# Container name
container = Config.get('DEFAULT', 'container')
#Name of the database user
user1= Config.get('DEFAULT', 'user')
#Server Password
password1= Config.get('DEFAULT', 'password')
#Hostname
host1= Config.get('DEFAULT', 'host')
#Port number
port1= Config.get('DEFAULT', 'port')
#Name of the database created
database1= Config.get('DEFAULT', 'database')



cnx = mysql.connector.connect(user=user1, password=password1, host=host1, port=port1, database=database1)
cursor=cnx.cursor()
sno=0
blob_service = BlockBlobService(account_name=account, account_key=key)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    sno=0
    if request.method == 'POST':
     file = request.files['file']
     filename = secure_filename(file.filename)
     fileextension = filename.rsplit('.',1)[1]
     fn = os.path.basename(file.filename)
     
     try:
            
            blob_service.create_blob_from_stream(container, filename, file)
            print(fn)
            cursor.execute("insert into filenames(sno, filename) values(%s,%s)",(sno,fn))
            cnx.commit()
            sno=sno+1
            
     except Exception:
            print('Exception'+ Exception) 

             
    return render_template('uploadfile.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0')




# In[ ]:
