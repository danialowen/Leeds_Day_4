# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:06:09 2018

@author: gydwo
"""

import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv

num_of_agents = 10
num_of_iterations = 10
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

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


#ax.set_autoscale_on(False)

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
    
carry_on = True

def update(frame_number):
    
    fig.clear()   
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_iterations):
        random.shuffle(agents)
        for i in range (num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)   
        
               
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    matplotlib.pyplot.ylim(0, 100)
    matplotlib.pyplot.xlim(0, 100)
    
for x in range(num_of_agents):
    for z in range(x + 1,num_of_agents):
        distance = agents[x].distance_between(agents[z])
        print(distance)
   


animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)

matplotlib.pyplot.show()    