#!/usr/bin/env python
# coding: utf-8

# In[1]:
import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug import secure_filename
from azure.storage.blob import *
import string, random, requests

app = Flask(__name__, instance_relative_config=True)

# Account name
account = 'storage312'
# Azure Storage account access key 
key ='/zS1FjwekwDGVaq75p73pEDwuIT3oZZ5bZFRNcyLzwQZjQ/5limq27Bdmp8UymsaYv+Cg5DnNbxcDQbOe5oqzQ=='
# Container name
container ='container312'


blob_service = BlockBlobService(account_name='storage312', account_key='/zS1FjwekwDGVaq75p73pEDwuIT3oZZ5bZFRNcyLzwQZjQ/5limq27Bdmp8UymsaYv+Cg5DnNbxcDQbOe5oqzQ==')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
     file = request.files['file']
     filename = secure_filename(file.filename)
     fileextension = filename.rsplit('.',1)[1]
     try:
            blob_service.create_blob_from_stream(container, filename, file)
            
     except Exception:
            print('Exception=' + Exception) 
            pass
     ref =  'http://'+ account + '.blob.core.windows.net/' + container + '/' + filename
         
    return render_template('uploadfile.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0')




# In[ ]:
