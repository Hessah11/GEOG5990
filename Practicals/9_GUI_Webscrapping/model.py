#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: hessah

This code is created as part of an assignment for GEOG5990 
at University of Leeds.

The code is an Agent-Based Model which creates agents based on data scrapped
from the web and an environment that is read from an input text file.
The created agents interact with the environment and with each other, and these
interactions can be seen as an animation on the GUI window.

Note: If using Spyder to run this code, ensure that the iPython Console 
graphics setting is set to inline by navigating to Tools > Preferences >
 iPython Console > Graphics  (Restart Spyder if you make any changes)

"""
#
# Import required packages for Model to run
#

#Libraries needed for plotting and GUI
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.backends.backend_tkagg
import matplotlib.pyplot
import matplotlib.animation
import tkinter

#Library needed for random numbers
import random

#Libraries for web scrapping
import requests
import bs4

#Agent Framework library from created agentframework.py
import agentframework


#
#Variables needed for the model to run
#
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []
environment = []



#
# Code to read the agent data from a fike on the web and add the values to two
# array variables
#
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/'
                 'python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#Used to test the file was read properly
#print(td_ys)
#print(td_xs)

#
# Code to read the environment data from in.txt file and save it in an array
# with open() was used to avoid issue with manual file close as mentioned in
# thw slides
#
with open("in.txt") as dataset:
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
#
# For loop to initialise the agents using the data scrapped from the web.
#
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment,agents))

# Variable initialised to be used in the stopping condition of the animation
carry_on = True	

#
# function update used in the animation process of the agents interactions
#
def update(frame_number):
    
    fig.clear()   
    global carry_on

    #Randomise the order of the agents list at each iteration
    random.shuffle(agents)
    
    #loop through the list of agents and perform a move, eat and share action
    for i in range(num_of_agents):
        #Move the agent
        agents[i].move()
        #Eat from the environment
        agents[i].eat()
        #Share the resources aquired with neighbour agents in neighbourhood
        agents[i].share_with_neighbours(neighbourhood)
    #Variable to count count the number of agents who ate the required amount    
    eaten = 0
    #loop to check how much each agent ate
    for agent in agents :
        if agent.get_store() > 200:
            eaten +=1
    #Check if all agents had eaten the required amount        
    if eaten >= num_of_agents:
        #Loop to print how much each agent ate by printing the value of store
        for agent in agents :
            print(agent.get_store())
        #set carry_on to false to stop the animation
        carry_on = False 

    #Set the plot area ranges
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)

    #Plot the environment array values
    matplotlib.pyplot.imshow(environment)

    #loop to plot current location of agents
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].get_x(),agents[i].get_y())

#
# function used to manage the animation process
#
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 1000) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

#
# Function created to add to the run button in the menu to start the animation
#        
def run():
    #two possibile animation values with different iteration results in each
    """animation = matplotlib.animation.FuncAnimation(fig, update, interval=1,
                                                   repeat=False,
                                                   frames=num_of_iterations)"""
    animation = matplotlib.animation.FuncAnimation(fig, update,
                                                   frames=gen_function,
                                                   repeat=False)
    canvas.show()

#
# code to create, setup and initialise the animation and GUI 
#
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#Code to set the canvas area of the GUI
root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# Menu bar and buttons definitions
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Menu", menu=model_menu)
#Button to start animation
model_menu.add_command(label="Start model animation", command=run)
#Button to destroy (close) GUI window
model_menu.add_command(label="Close window", command=root.destroy) 

# this opens the GUI
tkinter.mainloop()     

#
# Code that was created to write the values of the environment variable after 
# completion of the animation
#
"""
f = open("out.txt", 'w')
for row in environment:
    f.write(','.join(map(str, row)))
f.close()
"""