#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 21:55:51 2018

@author: hessah
"""
import random

class Agent():
    def __init__ (self,environment,agents, y=None, x=None):
        self.environment = environment
        self.agents=agents
        self.store = 0
        if (y == None):
            self._y = random.randint(0,100)
        else:
            self._y = y
            
        if (x == None):
            self._x = random.randint(0,100)
        else:
            self._x = x

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
    
    def get_store(self): 
        return self.store   
        
    def set_x (self,x):
        self._x =x
    
    def set_y (self,y):
        self._y = y
     
    def set_store (self,store):
        self.store = store
        
    def eat(self): # can you make it eat what is left?
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
            
    def share_with_neighbours(self,neighbourhood):
        # Loop through the agents in self.agents .
        for agent in self.agents:
            # Calculate the distance between self and the current other agent:
            distance = self.distance_between(agent) 
            # If distance is less than or equal to the neighbourhood
            if distance <= neighbourhood:
                store_average = (self.get_store() + agent.get_store()) / 2
                self.set_store(store_average)
                agent.set_store(store_average)
                #print("sharing " + str(distance) + " " + str(store_average))



    def distance_between(self, agent_2):
        return (((self.get_x() - agent_2.get_x())**2) + 
    ((self.get_y() - agent_2.get_y())**2))**0.5        