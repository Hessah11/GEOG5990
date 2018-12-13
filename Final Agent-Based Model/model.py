#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 21:52:01 2018

@author: hessah
"""

import matplotlib
matplotlib.use('TkAgg')
import random
import operator
import matplotlib.pyplot
import agentframework
import matplotlib.animation
import tkinter
import requests
import bs4


#Variables needed for the model to run
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


#ax.set_autoscale_on(False)



r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)




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

# Make the agents.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
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

   
def run():
    #animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()
    
root = tkinter.Tk() 
root.wm_title("Model")

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 


tkinter.mainloop()     

#Open an out.txt file and write environment variable values to file then close it
f = open("out.txt", 'w')
for row in environment:
    f.write(','.join(map(str, row)))
f.close()

