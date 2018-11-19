#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:05:56 2018

@author: hessah
"""
import matplotlib

with open("in.txt") as dataset:
    environment = []
    for line in dataset:
        row = str.split(line,",")
        rowlist = []
        for value in row:
            rowlist.append(float(value))
        environment.append(rowlist)
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

