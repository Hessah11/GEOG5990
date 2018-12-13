#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: hessah

This code is created as part of an assignment for GEOG5990 
at University of Leeds.

This file is a required part of the ABM code and is responsible for the agent
initialisation and management.

"""
#Import required library random for random number generation
import random

#Start of definition of class Agent
class Agent():
    #
    # Function defined to initialise the agent with the passed parameters
    #
    def __init__ (self,environment,agents, y=None, x=None):
        self.environment = environment
        self.agents=agents
        self.store = 0
        # if y or x parameters are not passed, they will be randomly generated
        if (y == None):
            self._y = random.randint(0,100)
        else:
            self._y = y
            
        if (x == None):
            self._x = random.randint(0,100)
        else:
            self._x = x

    #
    # Function defined to manage the move operation of agents ensuring they
    # don't exceed the edge of the plot area by using the Torus solution
    #
    def move (self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
    #
    # function to return the value of x coordinate of the agent
    #
    def get_x (self):
        return self._x 
    #
    # function to return the value of y coordinate of the agent
    #    
    def get_y (self):
        return self._y
    
    #
    # function to return the value of store value of the agent
    #
    def get_store(self): 
        return self.store   

    #
    # function to set the value of x coordinate of the agent
    #        
    def set_x (self,x):
        self._x =x
    
    #
    # function to set the value of y coordinate of the agent
    #        
    def set_y (self,y):
        self._y = y
     
    #
    # function to set the store value of the agent
    #        
    def set_store (self,store):
        self.store = store
        
    #
    # function to perform the eat function of the agent until there is less
    # than 10 in the cell value
    #        
    def eat(self):
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10

    #
    # function to share the store value between the agent and its neighbours
    #                    
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

    #
    # function to return the eucledian distance between the agent and another
    #        
    def distance_between(self, agent_2):
        return (((self.get_x() - agent_2.get_x())**2) + 
    ((self.get_y() - agent_2.get_y())**2))**0.5        