
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 09:29:22 2019

@author: ishan
"""

import matplotlib.pyplot as plt
import numpy as np
import heapq
import math
import time

show_animation = True

# Taking the user inputs
sx = int(input('Enter the x-coordinate of Start point: '))        
sy = int(input('Enter the y-coordinate of Start point: '))        
gx = int(input('Enter the x-coordinate of Goal point: '))        
gy = int(input('Enter the y-coordinate of Goal point: ')) 
Robot_radius =  float(input('Enter the desired Robot radius : '))
clearance = float(input('Enter the desired Clearance : '))
# Creating obstacle map 
ox,oy = [],[]
explore_x,explore_y = [],[]
obstacle = np.zeros(shape=(250,150))
m = Robot_radius
start_time = time.time()
for x in range (0,250):    
    for y in range(0,150):
# Equations for rectangle        
        f1 = -y + (67.5 - m)
        f2 =  y - (112.5 +  m)
        f3 =  -x + (50 - m)
        f4 =  x - (100 + m)
 
 #Equations for circle
        f5 = (x - 190)**2 + (y - 130)**2 - (15+m)**2   
        
 #Equation for ellipse
        f6 = (1/(15+m)**2) * ((x - 140)**2) + (1/(6+m)**2) * ((y - 120)**2) - 1
        
 #Equation for polygon-triangle 1
        f7 = 38*x + 23*y - (m + 192.04)*44.42
        f8 = -y + 52 
        f9 = -38*x + 7*y + (-m + 150.88)*38.64
        
#Equation for polygon-traingle 2
        f10 = 2*x + 19*y - (m + 68.77)*19.10         
        f11 = -41*x -25*y  + (135.88 - m)*48.02
        f12 = 37*x -13*y  - (136.55 )*39.22
        
#Equation for polygon-part 3
        f13 = y - 52 
        f14 = 37*x - 20*y - (145.06 + m)*42.05
        f15 = -y + 15 - m
        f16 = -37*x + 13*y + (136.55)*39.22

#Equation for boundary 1:
        b1 = y - m
#Equation for boundary 2:
        b2 = x - m
#Equation for boundary 3:
        b3 = y - (150 - m)
#Equation for boundary 4:
        b4 = x - (250 - m)
        
        if (f1<=0 and f2<=0 and f3<=0 and f4<=0 or f5<=0 or f6<=0 or (f7<=0 and f8<=0 and f9<=0) or (f10<=0 and f11<=0 and f12<=0) or (f13<=0 and f14<=0 and f15<=0 and f16<=0) or b1<0 or b2<0 or b3>0 or b4>0):
            obstacle[x][y] = 1
            ox.append(x)
            oy.append(y)     

#plotting the obstacle map
plt.plot(ox,oy,".k")
plt.ylim((0,150))
plt.xlim((0,250))
# =============================================================================
c = clearance
cx,cy = [],[]
m = m + c
for x in range (0,250):    
    for y in range(0,150):
# Equations for rectangle        
        f1 = -y + (67.5 - m)
        f2 =  y - (112.5 +  m)
        f3 =  -x + (50 - m)
        f4 =  x - (100 + m)
 
 #Equations for circle
        f5 = (x - 190)**2 + (y - 130)**2 - (15+m)**2   
        
 #Equation for ellipse
        f6 = (1/(15+m)**2) * ((x - 140)**2) + (1/(6+m)**2) * ((y - 120)**2) - 1
        
 #Equation for polygon-triangle 1
        f7 = 38*x + 23*y - (m + 192.04)*44.42
        f8 = -y + 52 
        f9 = -38*x + 7*y + (-m + 150.88)*38.64
        
#Equation for polygon-traingle 2
        f10 = 2*x + 19*y - (m + 68.77)*19.10         
        f11 = -41*x -25*y  + (135.88 - m)*48.02
        f12 = 37*x -13*y  - (136.55 )*39.22
        
#Equation for polygon-part 3
        f13 = y - 52 
        f14 = 37*x - 20*y - (145.06 + m)*42.05
        f15 = -y + 15 - m
        f16 = -37*x + 13*y + (136.55)*39.22

#Equation for boundary 1:
        b1 = y - m
#Equation for boundary 2:
        b2 = x - m
#Equation for boundary 3:
        b3 = y - (150 - m)
#Equation for boundary 4:
        b4 = x - (250 - m)
        
        if (f1<=0 and f2<=0 and f3<=0 and f4<=0 or f5<=0 or f6<=0 or (f7<=0 and f8<=0 and f9<=0) or (f10<=0 and f11<=0 and f12<=0) or (f13<=0 and f14<=0 and f15<=0 and f16<=0) or b1<0 or b2<0 or b3>0 or b4>0):
            obstacle[x][y] = 1
            cx.append(x)
            cy.append(y)


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
        
        if (len(explore_x)) % 450 == 0:
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

if start in zip(ox,oy) or start in zip(cx,cy):
    print('Start node is in obstacle space.Please select another node.')
elif goal in zip(ox,oy) or goal in zip(cx,cy) :    
    print('Goal node is in obstacle space .Please select another node.')
else:
    path = dijkistra(start,goal, obstacle)   
    if path == None:
        print('Goal node is in obstacle space.Please select another node.')    
    else:    
        pathx = [path[i][0] for i in range(len(path))]
        pathy = [path[i][1] for i in range(len(path))]

        plt.plot(start[0], start[1], "Dm")
        plt.plot(goal[0], goal[1], "Dg")        
        plt.plot(explore_x,explore_y, "3c")
        plt.plot(pathx,pathy,"-r")
        plt.show()
        end_time = time.time()
        print('time elapsed:',abs(end_time - start_time))  
