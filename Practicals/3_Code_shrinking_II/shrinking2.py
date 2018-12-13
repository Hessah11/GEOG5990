import random
import operator
import matplotlib.pyplot


num_of_agents = 10
num_of_iterations=100
agents = []


for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

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
        # Check if off edge and adjust.
        if agents[i][0] < 0:
            agents[i][0] += 100
        if agents[i][1] < 0:
            agents[i][1] += 100
        if agents[i][0] > 100:
            agents[i][0] -= 100
        if agents[i][1] > 100:
            agents[i][1] -= 100

#answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1]- agents[1][1])**2))**0.5

matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()
