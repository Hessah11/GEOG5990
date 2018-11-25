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

#Variables needed for the model to run
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []

#Open the in.txt file and read the values into the environment variable
with open("in.txt") as dataset:
    environment = []
    #loop on each line in the opened file
    for line in dataset:
        #Split the values in the line using the ',' seperator
        row = str.split(line,",")
        rowlist = []
        #loop to append each value within the line to an array
        for value in row:
            rowlist.append(int(value))            
        #append the array of values in the line to the environment array
        environment.append(rowlist)

#Set the plot ranges
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)

#Plot the environment variable before processing
matplotlib.pyplot.imshow(environment)

#Show the plot
matplotlib.pyplot.show()

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))

# Start the iterations of actions
for j in range(num_of_iterations):
    #Randomise the order of the agents list at each iteration
    random.shuffle(agents)
    
    #loop through the list of agents
    for i in range(num_of_agents):
        #Move the agent
        agents[i].move()
        #Eat from the environment
        agents[i].eat()
        #Share the resources aquired with neighbour agents in neighbourhood
        agents[i].share_with_neighbours(neighbourhood)

#Set the plot ranges
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)

#Plot the environment after all processing iterations are completed
matplotlib.pyplot.imshow(environment)

#loop to plot final location of agents
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].get_x(),agents[i].get_y())

#Show the plot
matplotlib.pyplot.show()

#Open an out.txt file and write environment variable values to file then close it
f = open("out.txt", 'w')
for row in environment:
    f.write(','.join(map(str, row)))
f.close()
