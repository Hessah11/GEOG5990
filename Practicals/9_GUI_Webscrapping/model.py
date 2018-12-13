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
import matplotlib.animation

#Variables needed for the model to run
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


#ax.set_autoscale_on(False)


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

##Set the plot ranges
#matplotlib.pyplot.xlim(0, 99)
#matplotlib.pyplot.ylim(0, 99)

##Plot the environment variable before processing
#matplotlib.pyplot.imshow(environment)

##Show the plot
#matplotlib.pyplot.show()

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))

carry_on = True	

# Start the iterations of actions
def update(frame_number):
    
    fig.clear()   
    global carry_on

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
    eaten = 0
    for agent in agents :
        if agent.get_store() > 200:
            eaten +=1
            
    if eaten >= num_of_agents:
        
        for agent in agents :
            print(agent.get_store())
        carry_on = False 

    #Set the plot ranges
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)

    #Plot the environment after all processing iterations are completed
    matplotlib.pyplot.imshow(environment)

    #loop to plot final location of agents
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].get_x(),agents[i].get_y())
        #print(agents[i].get_x(),agents[i].get_y())

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 1000) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

   

     
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

#Show the plot
matplotlib.pyplot.show()

#Open an out.txt file and write environment variable values to file then close it
f = open("out.txt", 'w')
for row in environment:
    f.write(','.join(map(str, row)))
f.close()
