#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 21:55:51 2018

@author: hessah
"""
import random

class Agent():
    def __init__ (self,environment):
        self.environment = environment
        self.store = 0
        self._x=random.randint(0,99)
        self._y=random.randint(0,99)
    
    def move (self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
            
    def get_x (self):
        return self._x 
    def get_y (self):
        return self._y
                
    def set_x (self,x):
        self._x =x
    def set_y (self,y):
        self._y = y
        
    def eat(self): # can you make it eat what is left?
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10