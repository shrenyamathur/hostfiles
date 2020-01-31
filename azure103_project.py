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
account = 'storage3121'
# Azure Storage account access key 
key ='U0m94QTcXaDWwccWcql+MwxxZw+c+cNRNrm4kaYAfpZ5SI0hfeAJGP0omxTs5zAJ6XeKhT/3+4GCr+vqf+BMWA=='
# Container name
container ='container312'


blob_service = BlockBlobService(account_name='storage3121', account_key='U0m94QTcXaDWwccWcql+MwxxZw+c+cNRNrm4kaYAfpZ5SI0hfeAJGP0omxTs5zAJ6XeKhT/3+4GCr+vqf+BMWA==')

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




