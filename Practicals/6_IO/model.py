#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 21:52:01 2018

@author: hessah
"""
import random
import operator
import matplotlib.pyplot
import agentframework

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.get_x() - agents_row_b.get_x())**2) + 
    ((agents_row_a.get_y() - agents_row_b.get_y())**2))**0.5


num_of_agents = 10
num_of_iterations = 100
agents = []


with open("in.txt") as dataset:
    environment = []
    for line in dataset:
        row = str.split(line,",")
        rowlist = []
        for value in row:
            rowlist.append(int(value))
        environment.append(rowlist)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        agents[i].move()
        agents[i].eat()

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].get_x(),agents[i].get_y())
matplotlib.pyplot.show()



for agents_row_a in agents:
    for agents_row_b in agents:
        if agents_row_a != agents_row_b:
            distance = distance_between(agents_row_a, agents_row_b)
            #print(distance_between(agents_row_a, agents_row_b))

#Write environment to file
f = open("out.txt", 'w')
for row in environment:
#    for value in row
    	f.write(','.join(map(str, row)))
f.close()
