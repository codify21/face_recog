#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 08:40:42 2021

@author: macbookpro
"""

from flask import Flask
from app import views_face 

app = Flask(__name__)

app.add_url_rule('/base','base',views_face.base)

app.add_url_rule('/','index',views_face.index)

app.add_url_rule('/faceapp','faceapp',views_face.faceapp)#endpoint is gender

app.add_url_rule('/faceapp/gender','gender',views_face.gender,methods=['GET','POST'])


if __name__ == '__main__':
    app.run(host = '127.0.0.1',port=5000,debug=True)