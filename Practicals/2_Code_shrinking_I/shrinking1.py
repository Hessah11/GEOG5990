
import random
import operator
import matplotlib.pyplot

agents = []


agents.append([random.randint(0,99),random.randint(0,99)])
#y0
if random.random()<0.5:
        agents[0][0]+=1
else:
        agents[0][0]-=1

#x0
if random.random()<0.5:
        agents[0][1]+=1
else:
        agents[0][1]-=1



agents.append([random.randint(0,99),random.randint(0,99)])
if random.random()<0.5:
        agents[1][0]+=1
else:
       agents[1][0]-=1

if random.random()<0.5:
        agents[1][1]+=1
else:
        agents[1][1]-=1



print(max(agents))
print(max(agents, key=operator.itemgetter(1))) 
answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1]- agents[1][1])**2))**0.5
print(answer)


print(agents)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
maxAgent = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(maxAgent[1],maxAgent[0], color='red')
matplotlib.pyplot.show()
