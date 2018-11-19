import random
import operator
import matplotlib.pyplot
import time

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5

    
    
num_of_agents = 10
num_of_iterations = 100
agents = []

#variables to hold the maximum and minimum distance values (between agents)
maximumDistance=0.0
minimumDistance=100.0

# Create the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        # Move agent (y)
        if random.random()<0.5:
                agents[i][0]+=1
        else:
                agents[i][0]-=1
        # Move agent (x)
        if random.random()<0.5:
                agents[i][1]+=1
        else:
                agents[i][1]-=1
        # Check if off any edge and adjust using torus.
        if agents[i][0] < 0:
            agents[i][0] += 100
        if agents[i][1] < 0:
            agents[i][1] += 100
        if agents[i][0] > 100:
            agents[i][0] -= 100
        if agents[i][1] > 100:
            agents[i][1] -= 100



matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()


start = time.clock()

for j in range(num_of_agents):
    for i in range(num_of_agents):
        #Calculate the distance only if the two agents are different
        if (i != j):
            distance=distance_between(agents[j], agents[i])
            if (distance > maximumDistance):
                maximumDistance=distance
            if (distance < minimumDistance):
                minimumDistance=distance
            #print(distance_between(agents[j], agents[i]))

end = time.clock()
print("time = " + str(end - start))
print("The maximum distance between agents is " + str(maximumDistance))
print("The minimum distance between agents is " + str(minimumDistance))

