#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 08:46:30 2021

@author: macbookpro
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return ('Welcome to Face Recognition Project')
if __name__ == '__main__':
    app.run
