#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 08:42:12 2021

@author: macbookpro
"""

from flask import render_template,request
from flask import redirect,url_for
upload_folder='static/uploads/'
import os
from PIL import Image
from .utils import pipeline_model

def base():
    return render_template('base.html')

def index():
    return render_template('index.html')

def faceapp():
    return render_template('faceapp.html')

def getwidth(path):
    img= Image.open(path)
    size=img.size  # width & height
    aspect = size[0]/size[1]  # width/height
    w= 300*aspect

def gender():
    if request.method=="POST":
        f= request.files['image']
        filename=f.filename
        path=os.path.join(upload_folder,filename)
        f.save(path)
        # print('File saved succesfully')
        w=getwidth(path)
        #prediction(pass to pipeline model)
        pipeline_model(path,filename,color='bgr')
        return render_template('gender.html',fileupload=True,img_name=filename,wid=w)
    return render_template('gender.html',fileupload=False,img_name = 'faceai.png',wid=300)