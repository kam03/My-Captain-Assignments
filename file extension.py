# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 17:17:12 2021

@author: kamakshi
"""

print("Hello World")

x=input("The filename:")

file_extns= x.split(".")

print("The extension of the file is: " + repr(file_extns[-1]))
