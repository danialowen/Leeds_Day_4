# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 11:05:21 2018

@author: gydwo
"""

import csv
import matplotlib.pyplot
import random
import operator
import agentframework

num_of_agents = 10
num_of_iterations = 50
agents = []
neighbourhood = 20

f = open('in.txt', newline='')
environment = []
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist=[]
    for value in row:
        rowlist.append(value)
#        print(value)
    environment.append(rowlist)
f.close()


a = agentframework.Agent(environment, agents)

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))


# Move the agents.
for j in range(num_of_iterations):
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        
        
for x in range(num_of_agents):
    for z in range(x + 1,num_of_agents):
        distance = agents[x].distance_between(agents[z])
        print(distance)


"""#plot values
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()"""


matplotlib.pyplot.xlim(0,110)
matplotlib.pyplot.ylim(0,110)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()