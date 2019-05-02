#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 20:51:55 2019

@author: ishan
"""


import matplotlib.pyplot as plt
import numpy as np
import heapq
import math
import time

show_animation = True

# Creating obstacle map 
ox,oy = [],[]
explore_x,explore_y = [],[]
obstacle = np.zeros(shape=(250,150))
for x in range (0,250):    
    for y in range(0,150):

# Equations for rectangle        
        f1 = -y + 67.5
        f2 =  y - 112.5
        f3 =  -x + 50
        f4 =  x - 100
 
 #Equations for circle
        f5 = (x - 190)**2 + (y - 130)**2 - (15)**2   
        
 #Equation for ellipse
        f6 = (1/225) * ((x - 140)**2) + (1/36) * ((y - 120)**2) - 1
        
 #Equation for polygon-triangle 1
        f7 = 38*x + 23*y - 8530
        f8 = -y +52
        f9 = -38*x + 7*y +5830
        
#Equation for polygon-traingle 2
        f10 = 2*x + 19*y - 1314         
        f11 = -41*x -25*y + 6525
        f12 = 37*x -13*y -5355
        
#Equation for polygon-part 3
        f13 = y - 52
        f14 = 37*x - 20*y - 6101
        f15 = -y + 15
        f16 = -37*x + 13*y + 5355 
        if (f1<=0 and f2<=0 and f3<=0 and f4<=0 or f5<=0 or f6<=0 or (f7<=0 and f8<=0 and f9<=0) or (f10<=0 and f11<=0 and f12<=0) or (f13<=0 and f14<=0 and f15<=0 and f16<=0)): 
            obstacle[x][y] = 1
            ox.append(x)
            oy.append(y) 
            
for i in range(250):
        ox.append(i)
        oy.append(0)
        obstacle[i][0] = 1
for i in range(250):
        ox.append(i)
        oy.append(150)
        obstacle[i][149] = 1
for i in range(150):
        ox.append(0)
        oy.append(i)
        obstacle[0][i] = 1
for i in range(150):
        ox.append(250)
        oy.append(i)
        obstacle[249][i] = 1

# Taking the user inputs
sx = int(input('Enter the x-coordinate of Start point: '))        
sy = int(input('Enter the y-coordinate of Start point: '))        
gx = int(input('Enter the x-coordinate of Goal point: '))        
gy = int(input('Enter the y-coordinate of Goal point: '))        
start_time = time.time()
#plotting the obstacle map
plt.plot(ox,oy,".k")
plt.ylim((0,150))
plt.xlim((0,250))


def motion_model():
    steps = [[1,0,1],
             [0,1,1],
             [-1,0,1],
             [0,-1,1],
             [1,1,math.sqrt(2)],
             [1,-1,math.sqrt(2)],
             [-1,-1,math.sqrt(2)],
             [-1,1,math.sqrt(2)]]
    return steps


def dijkistra(start,goal, obstacle):
    
    start_node = (0,start,None)
    goal_node = (0,goal,None)
    
    motion = motion_model()
    
    open_list = []
    closed_list = []
    
    heapq.heappush(open_list,(start_node))
    obstacle[start_node[1][0]][start_node[1][1]] = 1

    while len(open_list)>0:
        current_node = heapq.heappop(open_list)
        heapq.heappush(closed_list,current_node)
        explore_x.append(current_node[1][0])
        explore_y.append(current_node[1][1])
        
        if (len(explore_x))%500 == 0:
            if show_animation:
                    plt.plot(explore_x,explore_y, "3c")
                    plt.pause(0.00001)
                
        if current_node[1] == goal_node[1] :
            print('Goal reached')
            path = []
            length = len(closed_list)
            current_pos = closed_list[length-1][1]
            path.append(current_pos)
            parent = closed_list[length-1][2]
            while parent != None: 
                for i in range(length):
                    X = closed_list[i]
                    if X[1] == parent:
                        parent = X[2]
                        current_pos = X[1]
                        path.append(current_pos)
            return path[::-1]    
                                                                             
        neighbors = []        
        for new_position in motion:
            
            # Get node position
            node_position = (current_node[1][0] + new_position[0],
                             current_node[1][1] + new_position[1])
            node_position_cost = current_node[0] + new_position[2]
            
# =============================================================================
#             node_heuristic_cost = 100 * (math.sqrt((goal_node[1][0] - node_position[0] )**2 + (goal_node[1][1] - node_position[1] )**2))
#             node_position_cost = node_position_cost + node_heuristic_cost
# =============================================================================
            
            node_parent = current_node[1]
            
            # Check within range
            if node_position[0] > (len(obstacle) - 1) or node_position[0] < 0 or node_position[1] > (len(obstacle[0]) -1) or node_position[1] < 0:
                continue
            
            # Check walkable terrain
            if obstacle[node_position[0]][node_position[1]] != 0:
                continue
            
            #Creating cost_map
            obstacle[node_position[0]][node_position[1]] = 1
    
            # Creating a new node and also assigning a parent
            new_node = (node_position_cost,node_position,node_parent)                
            neighbors.append(new_node)
            heapq.heappush(open_list,(new_node))
    
# =============================================================================
start = (sx, sy)
goal = (gx, gy)

if start in zip(ox,oy):
    print('Start node is in obstacle space.Please select another node.')
elif goal in zip(ox,oy) :    
    print('Goal node is in obstacle space .Please select another node.')
else:
    path = dijkistra(start,goal, obstacle)   
     
     
end_time = time.time()
print('time elapsed:',abs(end_time - start_time))  
print(path)  