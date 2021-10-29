# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 01:15:28 2021

@author: L
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! satu satu akhirnya bisa</p>"


